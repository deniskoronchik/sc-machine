#pragma once

#if defined (SC_STORAGE_SELF_BUILD)
# if defined (SC_PLATFORM_WIN)
#   define SC_STORAGE_API __declspec(dllexport)
# else
#   define SC_STORAGE_API
# endif
#else
# if defined (SC_PLATFORM_WIN)
#   define SC_STORAGE_API __declspec(dllimport)
# else
#   define SC_STORAGE_API
# endif
#endif
