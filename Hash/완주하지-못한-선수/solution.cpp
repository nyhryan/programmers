#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    unordered_map<string, int> dict{};

    for (const auto &name: participant) {
        dict[name] += 1;
    }

    for (const auto &name: completion) {
        dict[name] -= 1;
    }
    
    for (const auto &[name, count]: dict) {
        if (count > 0) return name;
    }

    return "";
}