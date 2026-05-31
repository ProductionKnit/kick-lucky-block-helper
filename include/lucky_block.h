#ifndef LUCKY_BLOCK_H
#define LUCKY_BLOCK_H

#include <string>
#include <vector>

class LuckyBlock {
public:
    LuckyBlock();
    void kick();
    std::string getRandomReward();
private:
    std::vector<std::string> rewards;
};

#endif