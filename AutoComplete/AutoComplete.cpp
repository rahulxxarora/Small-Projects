#include <iostream>
#include <string>

#define CHAR_TO_INDEX(c) ((int)c - (int)'a')
#define INDEX_TO_CHAR(i) (char(i+97))

using namespace std;

struct Trie_node
{
	int value;
	Trie_node *next[26];
}; 

struct Trie
{
	struct Trie_node *root;
};

struct Trie_node* getnode()
{
	struct Trie_node *temp = new Trie_node;

	temp->value = 0;
	for(int i=0;i<26;i++)
		temp->next[i] = NULL;

	return temp;
}

void initialize(struct Trie *head)
{
	head->root = getnode();
}

void insert(Trie *head, string str)
{
	int len = str.length();
	struct Trie_node *crawl = head->root;

	for(int level=0;level<len;level++)
	{
		int ind = CHAR_TO_INDEX(str[level]);

		if(!crawl->next[ind])
		{
			crawl->next[ind] = getnode();
		}

		crawl = crawl->next[ind];
	}

	crawl->value = 1;
}

int search(Trie *head, string str)
{
	int len = str.length();
	struct Trie_node *crawl = head->root;

	for(int level=0;level<len;level++)
	{
		int ind = CHAR_TO_INDEX(str[level]);

		if(!crawl->next[ind])
			break;

		crawl = crawl->next[ind];
	}

	return (crawl->value==1 && crawl!=NULL);
}

void AutoCompleteUtil(Trie_node *head, string str, char *temp, int idx)
{
	if(head->value==1)
	{
		temp[idx] = '\0';
		cout << str << temp << endl;
	}

	for(int i=0;i<26;i++)
	{
		if(head->next[i])
		{
			temp[idx] = INDEX_TO_CHAR(i);
			AutoCompleteUtil(head->next[i], str, temp, idx+1);
		}
	}
}

void AutoComplete(Trie *head, string str)
{
	int len = str.length();
	struct Trie_node *crawl = head->root;

	for(int level=0;level<len;level++)
	{
		int ind = CHAR_TO_INDEX(str[level]);

		crawl = crawl->next[ind];
	}

	char temp[101];

	AutoCompleteUtil(crawl, str, temp, 0);
}

int main()
{
	Trie trie;
	initialize(&trie);
	while(1)
	{
		string str;
		char temp;
		int ch;
		cout << "\n";
		cout << "1.Insert\n";
		cout << "2.Search\n";
		cout << "3.AutoComplete\n";
		cout << "Enter choice : ";
		cin >> ch;
		switch(ch)
		{
			case 1 : cout << "Enter string : ";
					 cin >> str;
					 insert(&trie, str);
					 break;
			case 2 : cout << "Enter string : ";
					 cin >> str;
					 (search(&trie, str))?cout << "Found\n":cout << "Not found\n";
					 break;
			case 3 : while(temp!='\n')
					 {
					     cin >> temp;
					     str.push_back(temp);
					     AutoComplete(&trie, str);
					 }
					 break;
		}
	}
	return 0;
}