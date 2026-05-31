#include "lucky_block.h"
#include <cassert>

void testGetRandomReward() {
    LuckyBlock block;
    std::string reward = block.getRandomReward();
    assert(!reward.empty());
}

int main() {
    testGetRandomReward();
    return 0;
}