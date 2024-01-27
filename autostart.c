#include <stdio.h>
#include <windows.h>

int main() {
  FILETIME lastModifiedTime;
  HANDLE fileHandle;
  const char* filePath = "test.txt";

  while (1) {
    fileHandle = CreateFile(filePath, GENERIC_READ, FILE_SHARE_READ, NULL, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, NULL);
    if (fileHandle != INVALID_HANDLE_VALUE) {
      GetFileTime(fileHandle, NULL, NULL, &lastModifiedTime);
      CloseHandle(fileHandle);

      // Check if the file was modified
      // Compare lastModifiedTime with the previously stored value

      // TODO: Add your logic here

      // Store the current modified time for the next iteration
      // lastModifiedTime will be used in the next iteration
    }

    Sleep(5000); // Sleep for 5 seconds
  }

  return 0;
}
