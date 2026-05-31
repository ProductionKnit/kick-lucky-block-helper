#include "lucky_block.h"
#include "roblox_interface.h"
#include <iostream>

int main() {
    LuckyBlock block;
    RobloxInterface roblox;

    roblox.sendChatMessage("Kicking lucky block...");
    block.kick();

    std::string reward = block.getRandomReward();
    roblox.sendChatMessage("You got: " + reward);

    return 0;
}