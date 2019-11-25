# Kewpyp [Keyword extraction from past year papers]
A web app to tell you which concepts seem to be important based on past year papers
 You can test the beta version here: http://kewpyp.herokuapp.com/apidocs/#/default/post_predict_file


## Heroku Commands

```
heroku create kewpyp
heroku container:push web --app kewpyp
heroku container:release web --app kewpyp
```

