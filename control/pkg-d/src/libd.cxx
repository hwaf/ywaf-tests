#include "libd.h"
#include "pkg-a/liba.h"
#include "pkg-b/libb.h"
#include "pkg-c/libc.h"

#include <iostream>

extern "C" {
  void my_complib_init() __attribute__((constructor));

  void my_complib_init() {
    std::cout << "my-complib-init...\n"
              << liba::print() << "\n"
              << libb::print() << "\n"
              << libc::print() << "\n"
              << "my-complib-init...[done]\n"
              << std::flush;
  }
}

namespace libd {
  std::string print() {
    return "hello from libd";
  }
}
