#include <string>
#include <iostream>
using namespace std;

class Solution{
public:
  string mergeAlternatively(string word1, string word2) {
    /***
     * The problem is merge alternating letters into a string
     * IE word1 = hello
     * IE word2 = world
     * EXPECTED OUTPUT = hweolrllod
     * IE w1 = yo
     * IE w2 = gabba
     * EXP OUT = ygoabba
    */
    // algo
    // 0. init vars
    // 0a. number of iterations would be len w1 + len w2
    // 1. start iters, if even and exists w1[i] 
    // 2. iters cont, if odd and exists w2[i]
    // 3. append rest of longer word
    // 4. return string
    string strHold = "";
    int ptr1 = 0, ptr2 = 0;
    int iters = word1.length() + word2.length();
    for (int i = 0; i < iters; i++) {
      if (i % 2 == 0 && word1[ptr1]) {
        strHold += word1[ptr1];
        ptr1++;
      } else if (i % 2 == 1 && word2[ptr2]) {
        strHold += word2[ptr2];
        ptr2++;
      }
    }

    while (word1[ptr1]) {
      strHold += word1[ptr1];
      ptr1++;
    }
    
    while (word2[ptr2]) {
      strHold += word2[ptr2];
      ptr2++;
    }
    return strHold;
  }
};

int main() {
  string w1;
  string w2;
  Solution sol;
  cout << "Enter first word: ";
  cin >> w1;
  cout << "Enter second word: ";
  cin >> w2;
  string solution = sol.mergeAlternatively(w1, w2);
  cout << solution;
  return 0;
}