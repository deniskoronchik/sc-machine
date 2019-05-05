#include "sc_segment.hpp"

#include <iostream>


bool ScSegment::ElementLock::TryLock(size_t attemptsNum)
{
  bool expected = false;
  size_t attempt = 0;
  while (attempt < attemptsNum &&
         !m_lock.compare_exchange_weak(expected, true,
                                       std::memory_order_release,
                                       std::memory_order_relaxed))
  {
    expected = false;
    ++attempt;
  }

  return attempt < attemptsNum;
}

void ScSegment::ElementLock::Lock()
{
  size_t i = 0;
  while (!TryLock(1))
  {
    if (i % 10 == 0)
      std::this_thread::yield();
  }
}

void ScSegment::ElementLock::Unlock()
{
  m_lock.store(false);
}

bool ScSegment::ElementLock::IsLocked() const
{
  return m_lock.load(std::memory_order_relaxed);
}
