#include <cstdio>
#include <cstring>
#include <string>
#include <cstdlib>
#include <iostream>
#include <map>

#include <limits>

#define SIZE 1024

using namespace std;

#define TYPE_NULL_TERMINATED_STRING 0
#define TYPE_SIZED_STRING 1
#define HEADER "CONTENT: "

class NullTerminatedString {
public:
  int type;
  void *data;

  NullTerminatedString() {};

  NullTerminatedString(char* buf) {
    this->type = TYPE_NULL_TERMINATED_STRING;
    this->data = strdup(buf);
  }

  virtual ~NullTerminatedString() {
    free(this->data);
  }

  virtual char* c_str() {
    return (char*)data;
  }

  virtual int size() {
    return strlen((const char*)data);
  }

  /*virtual*/ void update(char* buf) {
    free(this->data);
    this->data = strdup(buf);
  }

  void print() {
    char buf[size() + strlen(HEADER) + 1];
    strcpy(buf, HEADER);
    strcat(buf, c_str());

    printf("%s", buf);
  }
};

class StringMetadata {
public:
  int size;
  char* buf;

  StringMetadata(int size, char* buf) {
    this->size = size;
    this->buf = strdup(buf);
  }
  ~StringMetadata() {
    free(this->buf);
  }
};

class SizedString: public NullTerminatedString {
  public:
    SizedString(char* buf) {
      this->type = TYPE_SIZED_STRING;
      this->data = new StringMetadata(strlen(buf), buf);;
    }

    ~SizedString() {
      delete((StringMetadata*)this->data);
    }

    char* c_str() {
      return ((StringMetadata*)this->data)->buf;
    }

    int size() {
      return ((StringMetadata*)this->data)->size;
    }

    void update(char* buf) {
      ((StringMetadata*)this->data)->buf = strdup(buf);
      ((StringMetadata*)this->data)->size = strlen(buf);
    }
};

// Global variable
map<string, NullTerminatedString*> string_map;

void fgets_strip(char* buf, size_t size, FILE* fp) {
  fgets(buf, size, fp);
  if (buf[strlen(buf) - 1] == '\n')
    buf[strlen(buf) - 1] = '\0';
}

void print_banner() {
  cout << endl
       << "1. create" << endl
       << "2. update" << endl
       << "3. read" << endl
       << "4. exit" << endl;
}

void create() {
  std::string id, content;
  int type;
  cout << "Type(0: NullTerminatedString, 1: SizedString)?" << endl;
  if (!(cin >> type) ||
      (type != TYPE_SIZED_STRING &&
      type != TYPE_NULL_TERMINATED_STRING)) {
    cout << "Error: Not supported type" << endl;
    return;
  }

  cout << "ID(length < 1024)?" << endl;
  cin >> id;
  if (id.size() >= 1024) {
    cout << "Error: String is too big" << endl;
    return;
  }

  cout << "Content(length < 1024)?" << endl;
  cin >> content;
  if (content.size() >= 1024) {
    cout << "Error: String is too big" << endl;
    return;
  }

  if (type == TYPE_SIZED_STRING) {
    string_map[id] = new SizedString((char*)content.c_str());
  }
  else {
    string_map[id] = new NullTerminatedString((char*)content.c_str());
  }
  cout << "Successfully create string!!" << endl;
}

void update() {
  std::string id;
  cout << "ID to change?" << endl;
  cin >> id;
  map<string, NullTerminatedString*>::iterator it = string_map.find(id);
  if (string_map.find(id) == string_map.end()) {
    cout << "Error: No such string" << endl;
    return;
  }

  std::string content;
  cout << "Content to change?" << endl;
  cin >> content;

  (*it).second->update((char*) content.c_str());
  cout << "Successfully updated!" << endl;
}

void read() {
  std::string id;
  cout << "ID to read?" << endl;
  cin >> id;
  map<string, NullTerminatedString*>::iterator it = string_map.find(id);
  if (string_map.find(id) == string_map.end()) {
    cout << "Error: No such string" << endl;
    return;
  }

  (*it).second->print();
  printf("\n");
}

int main() {
  setvbuf(stdin, NULL, _IONBF, 0);
  setvbuf(stdout, NULL, _IONBF, 0);

  cout << "Welcome to string emulator" << endl;

  int choice;
  while(true) {
    print_banner();
    if (!(cin >> choice)) {
      cout << "Error: Fail to read menu" << endl;
      break;
    }
    switch(choice) {
      case 1:
        create();
        break;
      case 2:
        update();
        break;
      case 3:
        read();
        break;
      case 4:
        cout << "Bye" << endl;
        exit(0);
      default:
        cout << "No such command" << endl;
    }
  }
}
