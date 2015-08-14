#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <fstream>
#include <sstream>
#include <map>
#include <set>

#include <string.h>

using namespace std;

class SummaryTool
{
	public:

	vector<string> split_content(string str, char delimiter) 
	{
  		vector<string> arr;
  		stringstream ss(str); 
  		string tok;
  
  		while(getline(ss, tok, delimiter)) 
  		{
    		arr.push_back(tok);
  		}
  
  		return arr;
  	}

	float sentences_intersection(string a, string b)
	{
		vector <string> A = split_content(a, ' ');
		vector <string> B = split_content(b, ' ');
		
		if(A.size()+B.size()==0)
			return 0;

		vector <string> C (A.size()+B.size());

		set <string> A_set,B_set,C_set;
		set <string>::iterator it;

		for(int i=0;i<A.size();i++)
    		A_set.insert(A[i]);

    	for(int i=0;i<B.size();i++)
    		B_set.insert(B[i]);

    	A_set.erase("I");
    	A_set.erase("am");
    	A_set.erase("the");
    	A_set.erase("is");
    	A_set.erase("of");
    	A_set.erase("was");
    	A_set.erase("and");
    	A_set.erase("on");
    	A_set.erase("a");
    	A_set.erase("an");
    	
    	B_set.erase("I");
    	B_set.erase("am");
    	B_set.erase("the");
    	B_set.erase("is");
    	B_set.erase("of");
    	B_set.erase("was");
    	B_set.erase("and");
    	B_set.erase("on");
    	B_set.erase("a");
    	B_set.erase("an");

		vector <string>::iterator it2 = set_intersection(A_set.begin(), A_set.end(), B_set.begin(), B_set.end(), C.begin());

		C.erase(it2, C.end());

		for(int i=0;i<C.size();i++)
    		C_set.insert(C[i]);

		float C_size = C_set.size();
		float A_size = A_set.size();
		float B_size = B_set.size();

		float ans = C_size/(A_size+B_size);
		
		return ans;
	}

	string format_sentence(string str)
	{
		int i=0,len=str.length();

		while(i<len)
		{
    		if(str[i]>='A'&&str[i]<='Z'||str[i]>='a'&&str[i]<='z'||str[i]==' ')
    		{
        		i++;
    		}
    		else
    		{
        		str.erase(i,1);
        		len--;
    		}
		}

		return str;
	}

	string remove_spaces(string str)
	{
		int i=0;
		for(i=0;i<str.length();i++)
			if(str[i]!=' ')
				break;
		return str.substr(i, str.length());
	}

	map<string, float> get_sentences_rank(string content, string title)
	{
		vector <string> arr = split_content(content, '.');

		int n = arr.size();
		float mat[n][n];

		for(int i=0;i<n;i++)
			for(int j=0;j<n;j++)
				mat[i][j] = 0.0;

		for(int i=0;i<n;i++)
		{
			for(int j=0;j<n;j++)
			{
				string a = remove_spaces(arr[i]);
				string b = remove_spaces(arr[j]);
				mat[i][j] = sentences_intersection(a, b);
			}
		}

		map <string, float> sentences_dic;

		for(int i=0;i<n;i++)
		{
			float score = 0;
			for(int j=0;j<n;j++)
			{
				if(i==j)
					continue;
				score += mat[i][j];
			}
			string temp = format_sentence(arr[i]);
			//cout << arr[i] << " " << score << endl;	
			sentences_dic[temp] = score;
		}

		return sentences_dic;
	}

	string get_best_sentence(string paragraph, map<string, float> sentences_dic)
	{
		vector <string> arr = split_content(paragraph, '.');

		if(arr.size()<=2)
			return "";

		string best_sentence = "";
		float max = 0;

		for(int i=0;i<arr.size();i++)
		{
			string temp = format_sentence(arr[i]);
			if(sentences_dic[temp]>max)
			{
				max = sentences_dic[temp];
				best_sentence = temp;
			}
		}

		return best_sentence; 
	}

	string get_summary(string content, string title, map<string, float> sentences_dic)
	{
		vector <string> arr = split_content(content, '\n');

		string summary;

		for(int i=0;i<arr.size();i++)
		{
			string temp = get_best_sentence(arr[i], sentences_dic);
			summary += temp;
		}

		return summary;
	}
};

int main()
{
	SummaryTool ob;

	string content, line;
	string title = "This is a test";
	ifstream ip ("data.txt");

	if(ip.is_open())
	{
		while(getline(ip, line, '\0'))
    	{
      		content += line;
    	}
    	ip.close();	
	}

	map <string, float> sentences_dic = ob.get_sentences_rank(content, title);

	string summary = ob.get_summary(content, title, sentences_dic);

	cout << "Sumamry : " << endl << summary << endl;

	return 0;
}