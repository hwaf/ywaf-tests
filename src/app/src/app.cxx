#include "liba/liba.h"
#include "libb/libb.h"

#include <iostream>

int main() {
  std::cout << "=== app ===\n"
            << "liba: " << liba::print() << "\n"
            << "libb: " << libb::print() << "\n"
            << std::flush;
}

