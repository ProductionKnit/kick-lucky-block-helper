#include "lucky_block.h"
#include <cstdlib>
#include <ctime>

LuckyBlock::LuckyBlock() {
    rewards = {
        "Diamonds", "Coins", "Sword", "Speed Boost", "Nothing"
    };
    std::srand(std::time(0));
}

void LuckyBlock::kick() {
    // Simulate kicking a lucky block
}

std::string LuckyBlock::getRandomReward() {
    int index = std::rand() % rewards.size();
    return rewards[index];
}