#pragma once

#include "sc_element.hpp"

#include <array>
#include <atomic>
#include <thread>

class ScSegment final
{
public:
  static size_t constexpr kElementsNum = 1 << 20;
  static size_t constexpr kThreadsNum = 1 << 5;

  struct ThreadSection
  {
    volatile std::thread::id m_lockThread;
  };

  class ElementLock
  {
  public:
    bool TryLock(size_t attemptsNum = 10);
    void Lock();
    void Unlock();
    bool IsLocked() const;

  private:
    std::atomic_bool m_lock;
  };

  class ElementMeta
  {

  private:
    ElementLock m_lock;
  };



private:
  std::array<ThreadSection, kThreadsNum> m_threadSections;
  std::array<ScElement, kElementsNum> m_elements;
  std::array<ElementMeta, kElementsNum> m_meta;
};
