#ifndef ROBLOX_INTERFACE_H
#define ROBLOX_INTERFACE_H

#include <string>

class RobloxInterface {
public:
    void sendChatMessage(const std::string& message);
    void simulateKeyPress(int keyCode);
};

#endif