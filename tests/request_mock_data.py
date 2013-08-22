# -*- coding: utf-8 -*-

mock_data = {
	"_wiki_request calls": {

		"{'inprop': 'url', 'titles': 'purpleberry', 'clcategories': 'Category:All disambiguation pages', 'prop': 'info|categories'}":
		{u'query': {u'normalized': [{u'to': u'Purpleberry', u'from': u'purpleberry'}], u'pages': {u'-1': {u'missing': u'', u'editurl': u'http://en.wikipedia.org/w/index.php?title=Purpleberry&action=edit', u'title': u'Purpleberry', u'contentmodel': u'wikitext', u'pagelanguage': u'en', u'ns': 0, u'fullurl': u'http://en.wikipedia.org/wiki/Purpleberry'}}}},

		"{'srinfo': 'suggestion', 'srlimit': 1, 'srsearch': 'Menlo Park, New Jersey', 'list': 'search', 'srprop': '', 'limit': 1}":
		{u'query-continue': {u'search': {u'sroffset': 1}}, u'query': {u'search': [{u'ns': 0, u'title': u'Edison, New Jersey'}]}, u'warnings': {u'main': {u'*': u"Unrecognized parameter: 'limit'"}}},
		
		"{'inprop': 'url', 'titles': 'Menlo Park, New Jersey', 'clcategories': 'Category:All disambiguation pages', 'prop': 'info|categories'}":
		{u'query': {u'pages': {u'342479': {u'redirect': u'', u'lastrevid': 463208951, u'pageid': 342479, u'title': u'Menlo Park, New Jersey', u'editurl': u'http://en.	wikipedia.org/w/index.php?title=Menlo_Park,_New_Jersey&action=edit', u'counter': u'', u'length': 74, u'contentmodel': u'wikitext', u'pagelanguage': u'en', u'	touched': u'2013-08-06T02:49:09Z', u'ns': 0, u'fullurl': u'http://en.wikipedia.org/wiki/Menlo_Park,_New_Jersey'}}}},
	
		"{'explaintext': '', 'titles': 'Menlo Park, New Jersey', 'prop': 'extracts'}":
		{u'query': {u'pages': {u'342479': {u'extract': u'REDIRECT Edison, New Jersey', u'ns': 0, u'pageid': 342479, u'title': u'Menlo Park, New Jersey'}}}},
	
		"{'inprop': 'url', 'titles': u'Edison, New Jersey', 'clcategories': 'Category:All disambiguation pages', 'prop': 'info|categories'}":
		{u'query': {u'pages': {u'125414': {u'lastrevid': 567347824, u'pageid': 125414, u'title': u'Edison, New Jersey', u'editurl': u'http://en.wikipedia.org/w/index.	php?title=Edison,_New_Jersey&action=edit', u'counter': u'', u'length': 78472, u'contentmodel': u'wikitext', u'pagelanguage': u'en', u'touched': u'2013-08-	08T22:21:48Z', u'ns': 0, u'fullurl': u'http://en.wikipedia.org/wiki/Edison,_New_Jersey'}}}},
	
		"{'inprop': 'url', 'titles': 'Dodge Ram (disambiguation)', 'clcategories': 'Category:All disambiguation pages', 'prop': 'info|categories'}":
		{u'query': {u'pages': {u'18803364': {u'lastrevid': 567152802, u'pageid': 18803364, u'title': u'Dodge Ram (disambiguation)', u'editurl': u'http://en.wikipedia.	org/w/index.php?title=Dodge_Ram_(disambiguation)&action=edit', u'counter': u'', u'length': 702, u'contentmodel': u'wikitext', u'pagelanguage': u'en', u'touched	': u'2013-08-08T15:12:27Z', u'ns': 0, u'fullurl': u'http://en.wikipedia.org/wiki/Dodge_Ram_(disambiguation)', u'categories': [{u'ns': 14, u'title': u'	Category:All disambiguation pages'}]}}}},
	
		"{'rvparse': '', 'titles': 'Dodge Ram (disambiguation)', 'rvprop': 'content', 'rvlimit': 1, 'prop': 'revisions'}":
		{u'query-continue': {u'revisions': {u'rvcontinue': 556603298}}, u'query': {u'pages': {u'18803364': {u'ns': 0, u'pageid': 18803364, u'revisions': [{u'*': u'<p><b><	a href="/wiki/Dodge_Ram" title="Dodge Ram">Dodge Ram</a></b> is a collective nameplate for light trucks made by <a href="/wiki/Dodge" title="Dodge">Dodge</a>\n	</p>\n<ul><li><a href="/wiki/Dodge_Ramcharger" title="Dodge Ramcharger">Dodge Ramcharger</a> - full-size SUV based on the Ram chassis (first vehicle to use 	the Ram name)\n</li><li><a href="/wiki/Dodge_Ram_Van" title="Dodge Ram Van">Dodge Ram Van</a> - full-size van\n</li><li><a href="/wiki/Dodge_Mini_Ram" 	title="Dodge Mini Ram" class="mw-redirect">Dodge Mini Ram</a> - cargo version of the Dodge Caravan\n<ul><li>See also:\n<ul><li><a 	href="/wiki/Dodge_Caravan_C/V" title="Dodge Caravan C/V" class="mw-redirect">Dodge Caravan C/V</a>\n</li><li><a href="/wiki/Ram_C/V" title="Ram C/V" class="mw-	redirect">Ram C/V</a> (modern day equivalent)\n</li></ul>\n</li></ul>\n</li><li><a href="/wiki/Dodge_Ram_50" title="Dodge Ram 50" class="mw-redirect">Dodge Ram 50</a> - Dodge version of the Mitsubishi Mighty Max, predecessor to the Dakota\n</li></ul>\n<p>See also:\n</p>\n<ul><li><a href="/wiki/Dodge_D-Series" 	title="Dodge D-Series" class="mw-redirect">Dodge D-Series</a> - Ram\'s predecessor, page includes first Ram body style\n</li><li><a href="/wiki/Dodge_Rampage" 	title="Dodge Rampage">Dodge Rampage</a> - car-based pickup truck\n</li><li><a href="/wiki/Ram_Trucks" title="Ram Trucks">Ram (brand)</a> - truck brand based 	on the Ram pickup truck\n</li></ul>\n<table id="disambigbox" class="metadata plainlinks dmbox dmbox-disambig" style="" role="presentation">\n<tr>\n<td 	class="mbox-image" style="padding: 2px 0 2px 0.4em;"> <a href="/wiki/File:Disambig_gray.svg" class="image"><img alt="Disambiguation icon" src="//upload.	wikimedia.org/wikipedia/en/thumb/5/5f/Disambig_gray.svg/30px-Disambig_gray.svg.png" width="30" height="23" srcset="//upload.wikimedia.	org/wikipedia/en/thumb/5/5f/Disambig_gray.svg/45px-Disambig_gray.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/5/5f/Disambig_gray.svg/60px-	Disambig_gray.svg.png 2x" /></a></td>\n<td class="mbox-text" style="padding: 0.25em 0.4em; font-style: italic;"> This <a href="/wiki/Help:Disambiguation" 	title="Help:Disambiguation">disambiguation</a> page lists articles associated with the same title. <br/> <small>If an <a class="external text" href="//en.	wikipedia.org/w/index.php?title=Special:WhatLinksHere/Dodge_Ram_(disambiguation)&amp;namespace=0">internal link</a> led you here, you may wish to change the 	link to point directly to the intended article.</small> </td>\n</tr>\n</table>\n'}], u'title': u'Dodge Ram (disambiguation)'}}}},
	
		"{'srinfo': 'suggestion', 'srlimit': 1, 'srsearch': 'butteryfly', 'list': 'search', 'srprop': '', 'limit': 1}":
		{u'query-continue': {u'search': {u'sroffset': 1}}, u'query': {u'searchinfo': {u'suggestion': u'butterfly'}, u'search': [{u'ns': 0, u'title': u"Butterfly's Tongue"}	]}, u'warnings': {u'main': {u'*': u"Unrecognized parameter: 'limit'"}}},
	
		"{'inprop': 'url', 'titles': u'butterfly', 'clcategories': 'Category:All disambiguation pages', 'prop': 'info|categories'}":
		{u'query': {u'normalized': [{u'to': u'Butterfly', u'from': u'butterfly'}], u'pages': {u'48338': {u'lastrevid': 566847704, u'pageid': 48338, u'title': u'Butterfly',	 u'editurl': u'http://en.wikipedia.org/w/index.php?title=Butterfly&action=edit', u'counter': u'', u'length': 60572, u'contentmodel': u'wikitext', u'	pagelanguage': u'en', u'touched': u'2013-08-07T11:15:37Z', u'ns': 0, u'fullurl': u'http://en.wikipedia.org/wiki/Butterfly'}}}},

		"{'srinfo': 'suggestion', 'srlimit': 1, 'srsearch': 'Celtuce', 'list': 'search', 'srprop': '', 'limit': 1}":
		{u'query-continue': {u'search': {u'sroffset': 1}}, u'query': {u'search': [{u'ns': 0, u'title': u'Celtuce'}]}, u'warnings': {u'main': {u'*': u"Unrecognized parameter: 'limit'"}}},

		"{'inprop': 'url', 'titles': u'Celtuce', 'clcategories': 'Category:All disambiguation pages', 'prop': 'info|categories'}":
		{u'query': {u'pages': {u'1868108': {u'lastrevid': 562756085, u'pageid': 1868108, u'title': u'Celtuce', u'editurl': u'http://en.wikipedia.org/w/index.php?title=Celtuce&action=edit', u'counter': u'', u'length': 1662, u'contentmodel': u'wikitext', u'pagelanguage': u'en', u'touched': u'2013-08-17T03:30:23Z', u'ns': 0, u'fullurl': u'http://en.wikipedia.org/wiki/Celtuce'}}}},

		"{'explaintext': '', 'titles': u'Celtuce', 'prop': 'extracts'}":
		{u'query': {u'pages': {u'1868108': {u'extract': u'Celtuce (Lactuca sativa var. asparagina, augustana, or angustata), also called stem lettuce, celery lettuce, asparagus lettuce, or Chinese lettuce, IPA (UK,US) /\u02c8s\u025blt.\u0259s/, is a cultivar of lettuce grown primarily for its thick stem, used as a vegetable. It is especially popular in China, and is called wosun (Chinese: \u83b4\u7b0b; pinyin: w\u014ds\u016dn) or woju (Chinese: \u83b4\u82e3; pinyin: w\u014dj\xf9) (although the latter name may also be used to mean lettuce in general).\n\nThe stem is usually harvested at a length of around 15\u201320 cm and a diameter of around 3\u20134 cm. It is crisp, moist, and mildly flavored, and typically prepared by slicing and then stir frying with more strongly flavored ingredients.', u'ns': 0, u'pageid': 1868108, u'title': u'Celtuce'}}}},

		"{'exintro': '', 'titles': u'Celtuce', 'explaintext': '', 'prop': 'extracts'}":
		{u'query': {u'pages': {u'1868108': {u'extract': u'Celtuce (Lactuca sativa var. asparagina, augustana, or angustata), also called stem lettuce, celery lettuce, asparagus lettuce, or Chinese lettuce, IPA (UK,US) /\u02c8s\u025blt.\u0259s/, is a cultivar of lettuce grown primarily for its thick stem, used as a vegetable. It is especially popular in China, and is called wosun (Chinese: \u83b4\u7b0b; pinyin: w\u014ds\u016dn) or woju (Chinese: \u83b4\u82e3; pinyin: w\u014dj\xf9) (although the latter name may also be used to mean lettuce in general).\n\nThe stem is usually harvested at a length of around 15\u201320 cm and a diameter of around 3\u20134 cm. It is crisp, moist, and mildly flavored, and typically prepared by slicing and then stir frying with more strongly flavored ingredients.', u'ns': 0, u'pageid': 1868108, u'title': u'Celtuce'}}}},

		"{'gimlimit': 'max', 'iiprop': 'url', 'titles': u'Celtuce', 'generator': 'images', 'prop': 'imageinfo'}":
		{u'query': {u'pages': {u'22263385': {u'imagerepository': u'local', u'ns': 6, u'pageid': 22263385, u'imageinfo': [{u'url': u'http://upload.wikimedia.org/wikipedia/en/9/99/Question_book-new.svg', u'descriptionurl': u'http://en.wikipedia.org/wiki/File:Question_book-new.svg'}], u'title': u'File:Question book-new.svg'}, u'-1': {u'imagerepository': u'shared', u'ns': 6, u'imageinfo': [{u'url': u'http://upload.wikimedia.org/wikipedia/commons/8/87/Celtuce.jpg', u'descriptionurl': u'http://commons.wikimedia.org/wiki/File:Celtuce.jpg'}], u'missing': u'', u'title': u'File:Celtuce.jpg'}, u'-3': {u'imagerepository': u'shared', u'ns': 6, u'imageinfo': [{u'url': u'http://upload.wikimedia.org/wikipedia/commons/7/79/VegCorn.jpg', u'descriptionurl': u'http://commons.wikimedia.org/wiki/File:VegCorn.jpg'}], u'missing': u'', u'title': u'File:VegCorn.jpg'}, u'-2': {u'imagerepository': u'shared', u'ns': 6, u'imageinfo': [{u'url': u'http://upload.wikimedia.org/wikipedia/commons/d/dc/The_farmer%27s_market_near_the_Potala_in_Lhasa.jpg', u'descriptionurl': u'http://commons.wikimedia.org/wiki/File:The_farmer%27s_market_near_the_Potala_in_Lhasa.jpg'}], u'missing': u'', u'title': u"File:The farmer's market near the Potala in Lhasa.jpg"}}}, u'limits': {u'images': 500}},

		"{'titles': u'Celtuce', 'prop': 'extlinks', 'ellimit': 'max'}":
		{u'query': {u'pages': {u'1868108': {u'extlinks': [{u'*': u'http://ndb.nal.usda.gov/ndb/search/list'}, {u'*': u'http://ndb.nal.usda.gov/ndb/search/list?qlookup=11145&format=Full'}], u'ns': 0, u'pageid': 1868108, u'title': u'Celtuce'}}}, u'limits': {u'extlinks': 500}},

		"{'plnamespace': 0, 'titles': u'Celtuce', 'pllimit': 'max', 'prop': 'links'}":
		{u'query': {u'pages': {u'1868108': {u'ns': 0, u'pageid': 1868108, u'links': [{u'ns': 0, u'title': u'Calcium'}, {u'ns': 0, u'title': u'Carbohydrate'}, {u'ns': 0, u'title': u'Chinese language'}, {u'ns': 0, u'title': u'Dietary Reference Intake'}, {u'ns': 0, u'title': u'Dietary fiber'}, {u'ns': 0, u'title': u'Fat'}, {u'ns': 0, u'title': u'Folate'}, {u'ns': 0, u'title': u'Food energy'}, {u'ns': 0, u'title': u'Iron'}, {u'ns': 0, u'title': u'Lettuce'}, {u'ns': 0, u'title': u'Lhasa'}, {u'ns': 0, u'title': u'Magnesium in biology'}, {u'ns': 0, u'title': u'Manganese'}, {u'ns': 0, u'title': u'Niacin'}, {u'ns': 0, u'title': u'Pantothenic acid'}, {u'ns': 0, u'title': u'Phosphorus'}, {u'ns': 0, u'title': u'Pinyin'}, {u'ns': 0, u'title': u'Plant stem'}, {u'ns': 0, u'title': u'Potassium'}, {u'ns': 0, u'title': u'Protein (nutrient)'}, {u'ns': 0, u'title': u'Riboflavin'}, {u'ns': 0, u'title': u'Sodium'}, {u'ns': 0, u'title': u'Stir frying'}, {u'ns': 0, u'title': u'Thiamine'}, {u'ns': 0, u'title': u'Vegetable'}, {u'ns': 0, u'title': u'Vitamin A'}, {u'ns': 0, u'title': u'Vitamin B6'}, {u'ns': 0, u'title': u'Vitamin C'}, {u'ns': 0, u'title': u'Zinc'}], u'title': u'Celtuce'}}}, u'limits': {u'links': 500}},

		"{'rvparse': '', 'titles': u'Celtuce', 'rvprop': 'content', 'rvlimit': 1, 'prop': 'revisions'}":
		{u'query-continue': {u'revisions': {u'rvcontinue': 547842204}}, u'query': {u'pages': {u'1868108': {u'ns': 0, u'pageid': 1868108, u'revisions': [{u'*': u'<table class="metadata plainlinks ambox ambox-content ambox-Unreferenced" style="" role="presentation">\n<tr><td class="mbox-image"><div style="width: 52px;"><a href="/wiki/File:Question_book-new.svg" class="image"><img alt="Question book-new.svg" src="//upload.wikimedia.org/wikipedia/en/thumb/9/99/Question_book-new.svg/50px-Question_book-new.svg.png" width="50" height="39" srcset="//upload.wikimedia.org/wikipedia/en/thumb/9/99/Question_book-new.svg/75px-Question_book-new.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/9/99/Question_book-new.svg/100px-Question_book-new.svg.png 2x" /></a></div></td><td class="mbox-text" style=""><span class="mbox-text-span">This article <b>does not <a href="/wiki/Wikipedia:Citing_sources" title="Wikipedia:Citing sources">cite</a> any <a href="/wiki/Wikipedia:Verifiability" title="Wikipedia:Verifiability">references or sources</a></b>.<span class="hide-when-compact">  Please help <a class="external text" href="//en.wikipedia.org/w/index.php?title=Celtuce&amp;action=edit">improve this article</a> by <a href="/wiki/Help:Introduction_to_referencing/1" title="Help:Introduction to referencing/1">adding citations to reliable sources</a>. Unsourced material may be challenged and <a href="/wiki/Wikipedia:Verifiability#Burden_of_evidence" title="Wikipedia:Verifiability">removed</a>.</span>&#32;<small><i>(December 2009)</i></small><span class="hide-when-compact"> </span></span></td></tr></table><div class="thumb tright"><div class="thumbinner" style="width:302px;"><a href="/wiki/File:Celtuce.jpg" class="image"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/8/87/Celtuce.jpg/300px-Celtuce.jpg" width="300" height="135" class="thumbimage" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/8/87/Celtuce.jpg/450px-Celtuce.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/8/87/Celtuce.jpg/600px-Celtuce.jpg 2x" /></a>  <div class="thumbcaption"><div class="magnify"><a href="/wiki/File:Celtuce.jpg" class="internal" title="Enlarge"><img src="//bits.wikimedia.org/static-1.22wmf12/skins/common/images/magnify-clip.png" width="15" height="11" alt="" /></a></div>Celtuce stems &amp; heads</div></div></div>\n<p><b>Celtuce</b> (<i>Lactuca sativa</i> var. <i>asparagina</i>, <i>augustana</i>, or <i>angustata</i>), also called <b>stem lettuce</b>, <b>celery lettuce</b>, <b>asparagus lettuce</b>, or <b>Chinese lettuce</b>, IPA (UK,US) <span title="Representation in the International Phonetic Alphabet (IPA)" class="IPA">/\u02c8s\u025blt.\u0259s/</span>, is a cultivar of <a href="/wiki/Lettuce" title="Lettuce">lettuce</a> grown primarily for its thick <a href="/wiki/Plant_stem" title="Plant stem">stem</a>, used as a <a href="/wiki/Vegetable" title="Vegetable">vegetable</a>.  It is especially popular in China, and is called <i><b>wosun</b></i> (<a href="/wiki/Chinese_language" title="Chinese language">Chinese</a>&#58; <span lang="zh"><a href="//en.wiktionary.org/wiki/%E8%8E%B4" class="extiw" title="wiktionary:\u83b4">\u83b4</a><a href="//en.wiktionary.org/wiki/%E7%AC%8B" class="extiw" title="wiktionary:\u7b0b">\u7b0b</a></span>&#59;&#32;<a href="/wiki/Pinyin" title="Pinyin">pinyin</a>&#58; <em>w\u014ds\u016dn</em>) or <i><b>woju</b></i> (<a href="/wiki/Chinese_language" title="Chinese language">Chinese</a>&#58; <span lang="zh"><a href="//en.wiktionary.org/wiki/%E8%8E%B4" class="extiw" title="wiktionary:\u83b4">\u83b4</a><a href="//en.wiktionary.org/wiki/%E8%8B%A3" class="extiw" title="wiktionary:\u82e3">\u82e3</a></span>&#59;&#32;<a href="/wiki/Pinyin" title="Pinyin">pinyin</a>&#58; <em>w\u014dj\xf9</em>) (although the latter name may also be used to mean lettuce in general).\n</p>\n<div class="thumb tright"><div class="thumbinner" style="width:302px;"><a href="/wiki/File:The_farmer%27s_market_near_the_Potala_in_Lhasa.jpg" class="image"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/d/dc/The_farmer%27s_market_near_the_Potala_in_Lhasa.jpg/300px-The_farmer%27s_market_near_the_Potala_in_Lhasa.jpg" width="300" height="241" class="thumbimage" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/d/dc/The_farmer%27s_market_near_the_Potala_in_Lhasa.jpg/450px-The_farmer%27s_market_near_the_Potala_in_Lhasa.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/d/dc/The_farmer%27s_market_near_the_Potala_in_Lhasa.jpg 2x" /></a>  <div class="thumbcaption"><div class="magnify"><a href="/wiki/File:The_farmer%27s_market_near_the_Potala_in_Lhasa.jpg" class="internal" title="Enlarge"><img src="//bits.wikimedia.org/static-1.22wmf12/skins/common/images/magnify-clip.png" width="15" height="11" alt="" /></a></div>Celtuce (foreground) for sale in <a href="/wiki/Lhasa" title="Lhasa">Lhasa</a></div></div></div>\n<table class="infobox" style="font-size: 88%; text-align: left; width: 22em; line-height: 1.5em">\n<caption style="font-size: 125%; font-weight: bold"> Celtuce, raw\n\n</caption>\n<tr>\n<th colspan="2" style="text-align: center"> Nutritional value per 100&#160;g (3.5&#160;oz)\n</th></tr>\n<tr style="background-color: #e0e0e0">\n<th> <a href="/wiki/Food_energy" title="Food energy">Energy</a>\n</th>\n<td> 75&#160;kJ (18&#160;kcal)\n</td></tr>\n<tr>\n<th> <a href="/wiki/Carbohydrate" title="Carbohydrate">Carbohydrates</a>\n</th>\n<td> 3.65 g\n</td></tr>\n\n\n\n<tr>\n<th> - <a href="/wiki/Dietary_fiber" title="Dietary fiber">Dietary fiber</a>\n</th>\n<td> 1.7 g\n</td></tr>\n\n<tr>\n<th> <a href="/wiki/Fat" title="Fat">Fat</a>\n</th>\n<td> 0.3 g\n</td></tr>\n\n\n\n\n\n\n<tr>\n<th> <a href="/wiki/Protein_(nutrient)" title="Protein (nutrient)">Protein</a>\n</th>\n<td> 0.85 g\n</td></tr>\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n<tr>\n<td> <a href="/wiki/Vitamin_A" title="Vitamin A">Vitamin A</a> equiv.\n</td>\n<td> 175 \u03bcg (22%)\n</td></tr>\n\n\n\n\n<tr>\n<td> <a href="/wiki/Thiamine" title="Thiamine">Thiamine (vit. B<sub>1</sub>)</a>\n</td>\n<td> 0.055 mg (5%)\n</td></tr>\n<tr>\n<td> <a href="/wiki/Riboflavin" title="Riboflavin">Riboflavin (vit. B<sub>2</sub>)</a>\n</td>\n<td> 0.07 mg (6%)\n</td></tr>\n<tr>\n<td> <a href="/wiki/Niacin" title="Niacin">Niacin (vit. B<sub>3</sub>)</a>\n</td>\n<td> 0.55 mg (4%)\n</td></tr>\n<tr>\n<td> <a href="/wiki/Pantothenic_acid" title="Pantothenic acid">Pantothenic acid</a> (B<sub>5</sub>)\n</td>\n<td> 0.183 mg (4%)\n</td></tr>\n<tr>\n<td> <a href="/wiki/Vitamin_B6" title="Vitamin B6">Vitamin B<sub>6</sub></a>\n</td>\n<td> 0.05 mg (4%)\n</td></tr>\n<tr>\n<td> <a href="/wiki/Folate" title="Folate" class="mw-redirect">Folate</a> (vit. B<sub>9</sub>)\n</td>\n<td> 46 \u03bcg (12%)\n</td></tr>\n\n\n<tr>\n<td> <a href="/wiki/Vitamin_C" title="Vitamin C">Vitamin C</a>\n</td>\n<td> 19.5 mg (23%)\n</td></tr>\n\n\n\n\n\n<tr>\n<td> <a href="/wiki/Calcium#Nutrition" title="Calcium">Calcium</a>\n</td>\n<td> 39 mg (4%)\n</td></tr>\n<tr>\n<td> <a href="/wiki/Iron#Biological_role" title="Iron">Iron</a>\n</td>\n<td> 0.55 mg (4%)\n</td></tr>\n<tr>\n<td> <a href="/wiki/Magnesium_in_biology" title="Magnesium in biology">Magnesium</a>\n</td>\n<td> 28 mg (8%)\n</td></tr>\n<tr>\n<td> <a href="/wiki/Manganese#Biological_role" title="Manganese">Manganese</a>\n</td>\n<td> 0.688 mg (33%)\n</td></tr>\n<tr>\n<td> <a href="/wiki/Phosphorus#Biological_role" title="Phosphorus">Phosphorus</a>\n</td>\n<td> 39 mg (6%)\n</td></tr>\n<tr>\n<td> <a href="/wiki/Potassium#In_diet" title="Potassium">Potassium</a>\n</td>\n<td> 330 mg (7%)\n</td></tr>\n<tr>\n<td> <a href="/wiki/Sodium#Biological_role" title="Sodium">Sodium</a>\n</td>\n<td> 11 mg (1%)\n</td></tr>\n<tr>\n<td> <a href="/wiki/Zinc#Biological_role" title="Zinc">Zinc</a>\n</td>\n<td> 0.27 mg (3%)\n</td></tr>\n\n\n\n\n\n<tr style="background-color: #e0e0e0; font-size: 90%; text-align: center; padding: 4pt; line-height: 1.25em">\n<td colspan="2"> <a rel="nofollow" class="external text" href="http://ndb.nal.usda.gov/ndb/search/list?qlookup=11145&amp;format=Full">Link to USDA Database entry</a><br/>Percentages are roughly approximated<br>using <a href="/wiki/Dietary_Reference_Intake" title="Dietary Reference Intake">US recommendations</a> for adults.<br/><small>Source: <a rel="nofollow" class="external text" href="http://ndb.nal.usda.gov/ndb/search/list">USDA Nutrient Database</a></small>\n</td></tr></table>\n<p>The stem is usually harvested at a length of around 15\u201320&#160;cm and a diameter of around 3\u20134&#160;cm. It is crisp, moist, and mildly flavored, and typically prepared by slicing and then <a href="/wiki/Stir_frying" title="Stir frying">stir frying</a> with more strongly flavored ingredients.\n</p><p><br />\n</p>\n<table class="metadata plainlinks stub" style="background: transparent;" role="presentation"><tr>\n<td><a href="/wiki/File:VegCorn.jpg" class="image"><img alt="Stub icon" src="//upload.wikimedia.org/wikipedia/commons/thumb/7/79/VegCorn.jpg/40px-VegCorn.jpg" width="40" height="26" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/7/79/VegCorn.jpg/60px-VegCorn.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/7/79/VegCorn.jpg/80px-VegCorn.jpg 2x" /></a></td>\n<td><i>This <a href="/wiki/Vegetable" title="Vegetable">vegetable</a>-related article  is a <a href="/wiki/Wikipedia:Stub" title="Wikipedia:Stub">stub</a>.  You can help Wikipedia by <a class="external text" href="//en.wikipedia.org/w/index.php?title=Celtuce&amp;action=edit">expanding it</a>.</i><div class="noprint plainlinks hlist navbar mini" style="position: absolute; right: 15px; display: none;"><ul><li class="nv-view"><a href="/wiki/Template:Vegetable-stub" title="Template:Vegetable-stub"><span title="View this template" style="">v</span></a></li><li class="nv-talk"><a href="/wiki/Template_talk:Vegetable-stub" title="Template talk:Vegetable-stub"><span title="Discuss this template" style="">t</span></a></li><li class="nv-edit"><a class="external text" href="//en.wikipedia.org/w/index.php?title=Template:Vegetable-stub&amp;action=edit"><span title="Edit this template" style="">e</span></a></li></ul></div></td>\n</tr></table>\n'}], u'title': u'Celtuce'}}}},

			"{'list': 'search', 'srprop': '', 'srlimit': 10, 'limit': 10, 'srsearch': 'Barack Obama'}":
			{u'query-continue': {u'search': {u'sroffset': 10}}, u'query': {u'searchinfo': {u'totalhits': 12987}, u'search': [{u'ns': 0, u'title': u'Barack Obama'}, {u'ns': 0, u'title': u'Barack Obama, Sr.'}, {u'ns': 0, u'title': u'Presidency of Barack Obama'}, {u'ns': 0, u'title': u'Barack Obama presidential campaign, 2008'}, {u'ns': 0, u'title': u'List of federal judges appointed by Barack Obama'}, {u'ns': 0, u'title': u'Barack Obama in comics'}, {u'ns': 0, u'title': u'Political positions of Barack Obama'}, {u'ns': 0, u'title': u'Barack Obama on social media'}, {u'ns': 0, u'title': u'List of Batman: The Brave and the Bold characters'}, {u'ns': 0, u'title': u'Family of Barack Obama'}]}, u'warnings': {u'main': {u'*': u"Unrecognized parameter: 'limit'"}}},

			"{'list': 'search', 'srprop': '', 'srlimit': 3, 'limit': 3, 'srsearch': 'Porsche'}":
			{u'query-continue': {u'search': {u'sroffset': 3}}, u'query': {u'searchinfo': {u'totalhits': 5335}, u'search': [{u'ns': 0, u'title': u'Porsche'}, {u'ns': 0, u'title': u'Porsche in motorsport'}, {u'ns': 0, u'title': u'Porsche 911 GT3'}]}, u'warnings': {u'main': {u'*': u"Unrecognized parameter: 'limit'"}}},

			"{'srinfo': 'suggestion', 'srlimit': 10, 'srsearch': 'hallelulejah', 'list': 'search', 'srprop': '', 'limit': 10}":
			{u'query': {u'searchinfo': {u'suggestion': u'hallelujah'}, u'search': []}, u'warnings': {u'main': {u'*': u"Unrecognized parameter: 'limit'"}}},

			"{'srinfo': 'suggestion', 'srlimit': 10, 'srsearch': 'qmxjsudek', 'list': 'search', 'srprop': '', 'limit': 10}":
			{u'query': {u'search': []}, u'warnings': {u'main': {u'*': u"Unrecognized parameter: 'limit'"}}},
	},

	"data": {
		"celtuce.content": u"Celtuce (Lactuca sativa var. asparagina, augustana, or angustata), also called stem lettuce, celery lettuce, asparagus lettuce, or Chinese lettuce, IPA (UK,US) /\u02c8s\u025blt.\u0259s/, is a cultivar of lettuce grown primarily for its thick stem, used as a vegetable. It is especially popular in China, and is called wosun (Chinese: \u83b4\u7b0b; pinyin: w\u014ds\u016dn) or woju (Chinese: \u83b4\u82e3; pinyin: w\u014dj\xf9) (although the latter name may also be used to mean lettuce in general).\n\nThe stem is usually harvested at a length of around 15\u201320 cm and a diameter of around 3\u20134 cm. It is crisp, moist, and mildly flavored, and typically prepared by slicing and then stir frying with more strongly flavored ingredients.",

		"celtuce.summary": u"Celtuce (Lactuca sativa var. asparagina, augustana, or angustata), also called stem lettuce, celery lettuce, asparagus lettuce, or Chinese lettuce, IPA (UK,US) /\u02c8s\u025blt.\u0259s/, is a cultivar of lettuce grown primarily for its thick stem, used as a vegetable. It is especially popular in China, and is called wosun (Chinese: \u83b4\u7b0b; pinyin: w\u014ds\u016dn) or woju (Chinese: \u83b4\u82e3; pinyin: w\u014dj\xf9) (although the latter name may also be used to mean lettuce in general).\n\nThe stem is usually harvested at a length of around 15\u201320 cm and a diameter of around 3\u20134 cm. It is crisp, moist, and mildly flavored, and typically prepared by slicing and then stir frying with more strongly flavored ingredients.",

		"celtuce.images": [u'http://upload.wikimedia.org/wikipedia/en/9/99/Question_book-new.svg', u'http://upload.wikimedia.org/wikipedia/commons/8/87/Celtuce.jpg', u'http://upload.wikimedia.org/wikipedia/commons/7/79/VegCorn.jpg', u'http://upload.wikimedia.org/wikipedia/commons/d/dc/The_farmer%27s_market_near_the_Potala_in_Lhasa.jpg'],

		"celtuce.references": [u'http://ndb.nal.usda.gov/ndb/search/list', u'http://ndb.nal.usda.gov/ndb/search/list?qlookup=11145&format=Full'],

		"celtuce.links": [u'Calcium', u'Carbohydrate', u'Chinese language', u'Dietary Reference Intake', u'Dietary fiber', u'Fat', u'Folate', u'Food energy', u'Iron', u'Lettuce', u'Lhasa', u'Magnesium in biology', u'Manganese', u'Niacin', u'Pantothenic acid', u'Phosphorus', u'Pinyin', u'Plant stem', u'Potassium', u'Protein (nutrient)', u'Riboflavin', u'Sodium', u'Stir frying', u'Thiamine', u'Vegetable', u'Vitamin A', u'Vitamin B6', u'Vitamin C', u'Zinc'],

		"celtuce.html": u'<table class="metadata plainlinks ambox ambox-content ambox-Unreferenced" style="" role="presentation">\n<tr><td class="mbox-image"><div style="width: 52px;"><a href="/wiki/File:Question_book-new.svg" class="image"><img alt="Question book-new.svg" src="//upload.wikimedia.org/wikipedia/en/thumb/9/99/Question_book-new.svg/50px-Question_book-new.svg.png" width="50" height="39" srcset="//upload.wikimedia.org/wikipedia/en/thumb/9/99/Question_book-new.svg/75px-Question_book-new.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/9/99/Question_book-new.svg/100px-Question_book-new.svg.png 2x" /></a></div></td><td class="mbox-text" style=""><span class="mbox-text-span">This article <b>does not <a href="/wiki/Wikipedia:Citing_sources" title="Wikipedia:Citing sources">cite</a> any <a href="/wiki/Wikipedia:Verifiability" title="Wikipedia:Verifiability">references or sources</a></b>.<span class="hide-when-compact">  Please help <a class="external text" href="//en.wikipedia.org/w/index.php?title=Celtuce&amp;action=edit">improve this article</a> by <a href="/wiki/Help:Introduction_to_referencing/1" title="Help:Introduction to referencing/1">adding citations to reliable sources</a>. Unsourced material may be challenged and <a href="/wiki/Wikipedia:Verifiability#Burden_of_evidence" title="Wikipedia:Verifiability">removed</a>.</span>&#32;<small><i>(December 2009)</i></small><span class="hide-when-compact"> </span></span></td></tr></table><div class="thumb tright"><div class="thumbinner" style="width:302px;"><a href="/wiki/File:Celtuce.jpg" class="image"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/8/87/Celtuce.jpg/300px-Celtuce.jpg" width="300" height="135" class="thumbimage" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/8/87/Celtuce.jpg/450px-Celtuce.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/8/87/Celtuce.jpg/600px-Celtuce.jpg 2x" /></a>  <div class="thumbcaption"><div class="magnify"><a href="/wiki/File:Celtuce.jpg" class="internal" title="Enlarge"><img src="//bits.wikimedia.org/static-1.22wmf12/skins/common/images/magnify-clip.png" width="15" height="11" alt="" /></a></div>Celtuce stems &amp; heads</div></div></div>\n<p><b>Celtuce</b> (<i>Lactuca sativa</i> var. <i>asparagina</i>, <i>augustana</i>, or <i>angustata</i>), also called <b>stem lettuce</b>, <b>celery lettuce</b>, <b>asparagus lettuce</b>, or <b>Chinese lettuce</b>, IPA (UK,US) <span title="Representation in the International Phonetic Alphabet (IPA)" class="IPA">/\u02c8s\u025blt.\u0259s/</span>, is a cultivar of <a href="/wiki/Lettuce" title="Lettuce">lettuce</a> grown primarily for its thick <a href="/wiki/Plant_stem" title="Plant stem">stem</a>, used as a <a href="/wiki/Vegetable" title="Vegetable">vegetable</a>.  It is especially popular in China, and is called <i><b>wosun</b></i> (<a href="/wiki/Chinese_language" title="Chinese language">Chinese</a>&#58; <span lang="zh"><a href="//en.wiktionary.org/wiki/%E8%8E%B4" class="extiw" title="wiktionary:\u83b4">\u83b4</a><a href="//en.wiktionary.org/wiki/%E7%AC%8B" class="extiw" title="wiktionary:\u7b0b">\u7b0b</a></span>&#59;&#32;<a href="/wiki/Pinyin" title="Pinyin">pinyin</a>&#58; <em>w\u014ds\u016dn</em>) or <i><b>woju</b></i> (<a href="/wiki/Chinese_language" title="Chinese language">Chinese</a>&#58; <span lang="zh"><a href="//en.wiktionary.org/wiki/%E8%8E%B4" class="extiw" title="wiktionary:\u83b4">\u83b4</a><a href="//en.wiktionary.org/wiki/%E8%8B%A3" class="extiw" title="wiktionary:\u82e3">\u82e3</a></span>&#59;&#32;<a href="/wiki/Pinyin" title="Pinyin">pinyin</a>&#58; <em>w\u014dj\xf9</em>) (although the latter name may also be used to mean lettuce in general).\n</p>\n<div class="thumb tright"><div class="thumbinner" style="width:302px;"><a href="/wiki/File:The_farmer%27s_market_near_the_Potala_in_Lhasa.jpg" class="image"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/d/dc/The_farmer%27s_market_near_the_Potala_in_Lhasa.jpg/300px-The_farmer%27s_market_near_the_Potala_in_Lhasa.jpg" width="300" height="241" class="thumbimage" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/d/dc/The_farmer%27s_market_near_the_Potala_in_Lhasa.jpg/450px-The_farmer%27s_market_near_the_Potala_in_Lhasa.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/d/dc/The_farmer%27s_market_near_the_Potala_in_Lhasa.jpg 2x" /></a>  <div class="thumbcaption"><div class="magnify"><a href="/wiki/File:The_farmer%27s_market_near_the_Potala_in_Lhasa.jpg" class="internal" title="Enlarge"><img src="//bits.wikimedia.org/static-1.22wmf12/skins/common/images/magnify-clip.png" width="15" height="11" alt="" /></a></div>Celtuce (foreground) for sale in <a href="/wiki/Lhasa" title="Lhasa">Lhasa</a></div></div></div>\n<table class="infobox" style="font-size: 88%; text-align: left; width: 22em; line-height: 1.5em">\n<caption style="font-size: 125%; font-weight: bold"> Celtuce, raw\n\n</caption>\n<tr>\n<th colspan="2" style="text-align: center"> Nutritional value per 100&#160;g (3.5&#160;oz)\n</th></tr>\n<tr style="background-color: #e0e0e0">\n<th> <a href="/wiki/Food_energy" title="Food energy">Energy</a>\n</th>\n<td> 75&#160;kJ (18&#160;kcal)\n</td></tr>\n<tr>\n<th> <a href="/wiki/Carbohydrate" title="Carbohydrate">Carbohydrates</a>\n</th>\n<td> 3.65 g\n</td></tr>\n\n\n\n<tr>\n<th> - <a href="/wiki/Dietary_fiber" title="Dietary fiber">Dietary fiber</a>\n</th>\n<td> 1.7 g\n</td></tr>\n\n<tr>\n<th> <a href="/wiki/Fat" title="Fat">Fat</a>\n</th>\n<td> 0.3 g\n</td></tr>\n\n\n\n\n\n\n<tr>\n<th> <a href="/wiki/Protein_(nutrient)" title="Protein (nutrient)">Protein</a>\n</th>\n<td> 0.85 g\n</td></tr>\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n<tr>\n<td> <a href="/wiki/Vitamin_A" title="Vitamin A">Vitamin A</a> equiv.\n</td>\n<td> 175 \u03bcg (22%)\n</td></tr>\n\n\n\n\n<tr>\n<td> <a href="/wiki/Thiamine" title="Thiamine">Thiamine (vit. B<sub>1</sub>)</a>\n</td>\n<td> 0.055 mg (5%)\n</td></tr>\n<tr>\n<td> <a href="/wiki/Riboflavin" title="Riboflavin">Riboflavin (vit. B<sub>2</sub>)</a>\n</td>\n<td> 0.07 mg (6%)\n</td></tr>\n<tr>\n<td> <a href="/wiki/Niacin" title="Niacin">Niacin (vit. B<sub>3</sub>)</a>\n</td>\n<td> 0.55 mg (4%)\n</td></tr>\n<tr>\n<td> <a href="/wiki/Pantothenic_acid" title="Pantothenic acid">Pantothenic acid</a> (B<sub>5</sub>)\n</td>\n<td> 0.183 mg (4%)\n</td></tr>\n<tr>\n<td> <a href="/wiki/Vitamin_B6" title="Vitamin B6">Vitamin B<sub>6</sub></a>\n</td>\n<td> 0.05 mg (4%)\n</td></tr>\n<tr>\n<td> <a href="/wiki/Folate" title="Folate" class="mw-redirect">Folate</a> (vit. B<sub>9</sub>)\n</td>\n<td> 46 \u03bcg (12%)\n</td></tr>\n\n\n<tr>\n<td> <a href="/wiki/Vitamin_C" title="Vitamin C">Vitamin C</a>\n</td>\n<td> 19.5 mg (23%)\n</td></tr>\n\n\n\n\n\n<tr>\n<td> <a href="/wiki/Calcium#Nutrition" title="Calcium">Calcium</a>\n</td>\n<td> 39 mg (4%)\n</td></tr>\n<tr>\n<td> <a href="/wiki/Iron#Biological_role" title="Iron">Iron</a>\n</td>\n<td> 0.55 mg (4%)\n</td></tr>\n<tr>\n<td> <a href="/wiki/Magnesium_in_biology" title="Magnesium in biology">Magnesium</a>\n</td>\n<td> 28 mg (8%)\n</td></tr>\n<tr>\n<td> <a href="/wiki/Manganese#Biological_role" title="Manganese">Manganese</a>\n</td>\n<td> 0.688 mg (33%)\n</td></tr>\n<tr>\n<td> <a href="/wiki/Phosphorus#Biological_role" title="Phosphorus">Phosphorus</a>\n</td>\n<td> 39 mg (6%)\n</td></tr>\n<tr>\n<td> <a href="/wiki/Potassium#In_diet" title="Potassium">Potassium</a>\n</td>\n<td> 330 mg (7%)\n</td></tr>\n<tr>\n<td> <a href="/wiki/Sodium#Biological_role" title="Sodium">Sodium</a>\n</td>\n<td> 11 mg (1%)\n</td></tr>\n<tr>\n<td> <a href="/wiki/Zinc#Biological_role" title="Zinc">Zinc</a>\n</td>\n<td> 0.27 mg (3%)\n</td></tr>\n\n\n\n\n\n<tr style="background-color: #e0e0e0; font-size: 90%; text-align: center; padding: 4pt; line-height: 1.25em">\n<td colspan="2"> <a rel="nofollow" class="external text" href="http://ndb.nal.usda.gov/ndb/search/list?qlookup=11145&amp;format=Full">Link to USDA Database entry</a><br/>Percentages are roughly approximated<br>using <a href="/wiki/Dietary_Reference_Intake" title="Dietary Reference Intake">US recommendations</a> for adults.<br/><small>Source: <a rel="nofollow" class="external text" href="http://ndb.nal.usda.gov/ndb/search/list">USDA Nutrient Database</a></small>\n</td></tr></table>\n<p>The stem is usually harvested at a length of around 15\u201320&#160;cm and a diameter of around 3\u20134&#160;cm. It is crisp, moist, and mildly flavored, and typically prepared by slicing and then <a href="/wiki/Stir_frying" title="Stir frying">stir frying</a> with more strongly flavored ingredients.\n</p><p><br />\n</p>\n<table class="metadata plainlinks stub" style="background: transparent;" role="presentation"><tr>\n<td><a href="/wiki/File:VegCorn.jpg" class="image"><img alt="Stub icon" src="//upload.wikimedia.org/wikipedia/commons/thumb/7/79/VegCorn.jpg/40px-VegCorn.jpg" width="40" height="26" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/7/79/VegCorn.jpg/60px-VegCorn.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/7/79/VegCorn.jpg/80px-VegCorn.jpg 2x" /></a></td>\n<td><i>This <a href="/wiki/Vegetable" title="Vegetable">vegetable</a>-related article  is a <a href="/wiki/Wikipedia:Stub" title="Wikipedia:Stub">stub</a>.  You can help Wikipedia by <a class="external text" href="//en.wikipedia.org/w/index.php?title=Celtuce&amp;action=edit">expanding it</a>.</i><div class="noprint plainlinks hlist navbar mini" style="position: absolute; right: 15px; display: none;"><ul><li class="nv-view"><a href="/wiki/Template:Vegetable-stub" title="Template:Vegetable-stub"><span title="View this template" style="">v</span></a></li><li class="nv-talk"><a href="/wiki/Template_talk:Vegetable-stub" title="Template talk:Vegetable-stub"><span title="Discuss this template" style="">t</span></a></li><li class="nv-edit"><a class="external text" href="//en.wikipedia.org/w/index.php?title=Template:Vegetable-stub&amp;action=edit"><span title="Edit this template" style="">e</span></a></li></ul></div></td>\n</tr></table>\n',

		"barack.search": [u'Barack Obama', u'Barack Obama, Sr.', u'Presidency of Barack Obama', u'Barack Obama presidential campaign, 2008', u'List of federal judges appointed by Barack Obama', u'Barack Obama in comics', u'Political positions of Barack Obama', u'Barack Obama on social media', u'List of Batman: The Brave and the Bold characters', u'Family of Barack Obama'],

		"porsche.search": [u'Porsche', u'Porsche in motorsport', u'Porsche 911 GT3'],
	}
}