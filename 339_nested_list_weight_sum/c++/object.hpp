#pragma once

#include <variant>
#include <vector>

struct Object
{
    std::variant<int, std::vector<Object>> value;
};