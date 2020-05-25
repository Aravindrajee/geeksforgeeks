// C++ program to rearrange an array in minimum
// maximum form
#include <bits/stdc++.h>
using namespace std;

// Prints max at first position, min at second position
// second max at third position, second min at fourth
// position and so on.
void rearrange(long arr[], long n)
{
	// initialize index of first minimum and first
	// maximum element
	long max_idx = n - 1, min_idx = 0;

	// store maximum element of array
	long max_elem = arr[n - 1] + 1;

	// traverse array elements
	for (long i = 0; i < n; i++) {
		// at even index : we have to put maximum element
		if (i % 2 == 0) {
			arr[i] += (arr[max_idx] % max_elem) * max_elem;
			max_idx--;
		}

		// at odd index : we have to put minimum element
		else {
			arr[i] += (arr[min_idx] % max_elem) * max_elem;
			min_idx++;
		}
	}

	// array elements back to it's original form
	for (long i = 0; i < n; i++)
		arr[i] = arr[i] / max_elem;
}

// Driver program to test above function
int main()
{
	long t, n, *arr;
	cin>>t;
	while(t--) {
	    cin>>n;
	    arr = new(nothrow) long[n];
	    for(long i=0; i<n; i++) {
	        cin>>arr[i];
	    }
	    rearrange(arr, n);
	    for(long i=0; i<n; i++) {
	        cout<<arr[i]<<' ';
	    }
	    cout<<endl;
	    delete arr;
	}
}
