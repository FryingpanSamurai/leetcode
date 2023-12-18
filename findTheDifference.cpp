#include <iostream>
using namespace std;

class Solution {
public:
  char findTheDifference(string s, string t) {
    // string t is gen by random shuffle string s and add one more letter at random pos
    // return the letter that was added to t

    // algo
    // 0. init vars
    // THOUGHT: could create struct for all letters in s and compare count to letters in t
    // 1. loop through s and assign count for each letter in the string
    // 2. loop through t checking struct
    // 3. return found letter
    struct {
    } alphaStruct;
    for (int i = 0; i < s.length(); i++) {
      alphaStruct.s[i] += 1;
    }
  }
};

int main() {
  return 0;
}