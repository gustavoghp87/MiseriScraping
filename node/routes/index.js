const express = require('express');
const router = express.Router();

var objJSON = {"test1": "testing1", "test2": "testing2"}

router.get('/', async (req, res) => {
  console.log(req);
//  const posts = await Post.find({ $and: [{"socialNet":"fb"}, {"year":2048}]}).limit(11);
  res.render('index', {objJSON});
});


router.post('/search', async (req, res, next) => {

  var wordsBrute = req.body.words || '';
  console.log("...words... " + wordsBrute)
  var words = []
  words = wordsBrute.split(' ');
  var queryWords = []
  for (i=0; i<words.length; i++) {
    queryWords.push({
      'post'   :   new RegExp( words[i], 'i')
    })
  }
  console.log(queryWords)

  
  var c2009 = req.body.c2009 || '';
 

  objJSON = {}
  if (twIgnore == "on") {
    objJSON = { 
                $and: [{$and: [{  $and: queryWords,   $or: queryYears}], $or: [{ $or: querySnets }] }],
                $or:  [{  $or:  [{'user': 'Carlos Maslaton'}, {'user': 'CarlosMaslaton'}] }]
              }
  } else {
    objJSON = {
                $and: [{$and:  queryWords, $or: queryYears}],
                $or:  [{$or: querySnets}]
    }
    //console.log("without 3rd tw")
  }


  var view = {'view': 'one', 'other': 'two'}

  if (years[0] != null) {
    var posts = await Post.find(objJSON).limit(50).sort({'timest': 1});
    res.render('index', {posts} );
  } else {
    var posts = await Post.find({ $and: [{"socialNet":"fb"}, {"year":2048}]}).limit(1);
    res.render('index', {posts} );
  }
})

//res.send envía un string, res.render un sitio, res.json un json

///////////////////////////////////////////////////////////////////////


router.get('/maslastory', async (req, res) => {
  res.render('maslastory');
});


module.exports = router;


// router.post('/add', async (req, res, next) => {
//   const post = new Post(req.body);
//   await post.save();
//   res.redirect('/');
// });

// router.get('/turn/:id', async (req, res, next) => {
//   let { id } = req.params;
//   const post = await Post.findById(id);
//   post.status = !post.status;
//   await post.save();
//   res.redirect('/');
// });

// router.get('/delete/:id', async (req, res, next) => {
//   let { id } = req.params;
//   await Task.remove({_id: id});
//   res.redirect('/');
// });


//router.get('/search', async (req, res, next) => {
//  var wordsBrute = req.params.words || ''; funcionaba con get en frontend
