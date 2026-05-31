#include "roblox_interface.h"
#include <iostream>

void RobloxInterface::sendChatMessage(const std::string& message) {
    std::cout << "[Roblox Chat] " << message << std::endl;
}

void RobloxInterface::simulateKeyPress(int keyCode) {
    std::cout << "[Roblox] Simulated key press: " << keyCode << std::endl;
}