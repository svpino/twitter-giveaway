# Selecting The Winner of a Twitter Giveaway

This is an absolutely over-engineered solution to select the winner of a Twitter Giveaway I ran on August 18, 2020.

I didn't just want to select somebody randomly as any sane person would do. Instead, I tried to use the opportunity and throw some Deep Learning into the mix. 

But of course, there's no way to use Deep Learning in any useful way when the only thing you need is a freaking random number, so I decided to start doing silly things.

There are two pieces to this solution:

* The script `retweets.py`: Continuously retrieves the last 100 retweets of the giveaway tweet and stores them in CSV files. There's also a function in this script to combine all of these users into a single CSV file that's later used in the notebook.
* The `giveaway.ipynb` notebook: Contains all the code to select the winner.

If you are interested about all the trouble that I went through to avoid generating a simple random number, the notebook will walk you through the entire thing.

