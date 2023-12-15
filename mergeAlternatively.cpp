#include <string>
using namespace std;

class Solution{
public:
  string mergeAlternatively(string word1, string word2) {
    /***
     * The problem is merge alternating letters into a string
     * I.E. word1 = hello
     * I.E. word2 = world
     * EXPECTED OUTPUT = hweolrllod
    */
    // algo
    // 0. init vars
    // 1. find longer of the two strings (this will be our upper limit for our for loop)
    // 2. traverse through the longer of the two
    // 3. append even indexes of the new string holder with word1 letters and odd indexes with word2 letters
    // 4. output string holder
    string strHold = "";
  }
};