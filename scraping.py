def scrape_all():
   # Initiate headless driver for deployment
   browser = Browser("chrome", executable_path="chromedriver", headless=True)
   news_title, news_paragraph = mars_news(browser)
   # Run all scraping functions and store results in dictionary
   # Run all scraping functions and store results in dictionary
   data = {
         "news_title": news_title,
         "news_paragraph": news_paragraph,
         "featured_image": featured_image(browser),
         "facts": mars_facts(),
         "last_modified": dt.datetime.now()
   }
   if __name__ == "__main__":
      # If running as script, print scraped data
      print(scrape_all())
