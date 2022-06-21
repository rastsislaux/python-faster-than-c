#include <iostream>

int main(void) {
    for (int i = 1000; i > 0; i -= 7) {
        std::cout << i << " - 7 = " << i - 7 << '\n';
    }
    std::cout << "I'm a ghoul." << std::endl;
    return 0;
}