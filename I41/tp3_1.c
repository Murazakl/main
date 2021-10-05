#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef enum{
  TRUE = 1,
  FALSE = 0
} tbool;

tbool EstPalindrome(char *phrase);

int main(){
  tbool test = EstPalindrome("yohan");
  printf("Est-ce un palindrome: %s\n", test ? "Oui" : "Non");
}

tbool EstPalindrome(char *phrase){
  int t = strlen(phrase);
  int i = 0;
  while (i < t){
    if (phrase[i] != phrase[t - i - 1])
      return FALSE;
    i++;
  }
  return TRUE;
}
