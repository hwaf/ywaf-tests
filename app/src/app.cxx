#include "pkg-a/liba.h"
#include "pkg-b/libb.h"

#include <iostream>

int main() {
  std::cout << "=== app ===\n"
            << "liba: " << liba::print() << "\n"
            << "libb: " << libb::print() << "\n"
            << std::flush;
}

