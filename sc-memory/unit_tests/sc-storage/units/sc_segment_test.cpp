#include "sc-memory/utils/sc_test.hpp"

#include "sc-storage/private/sc_segment.hpp"

#include <string>
#include <thread>

UNIT_TEST(ScSegment_ElementLock)
{
  SUBTEST_START(Lock/Unlock)
  {
    ScSegment::ElementLock lock;
    std::string value = "main_thread";

    lock.Lock();

    SC_CHECK(lock.IsLocked(), ());

    std::thread thread([&lock, &value]()
    {
      lock.Lock();
      value = "thread";
    });

    std::this_thread::sleep_for(std::chrono::milliseconds(1000));
    SC_CHECK_EQUAL(value, "main_thread", ());

    lock.Unlock();
    if (thread.joinable())
      thread.join();

    SC_CHECK_EQUAL(value, "thread", ());
  }
  SUBTEST_END()
}
