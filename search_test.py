from search import search, title_length, article_count, random_article, favorite_article, multiple_keywords, display_result
from search_tests_helper import get_print, print_basic, print_advanced, print_advanced_option
from wiki import article_titles
from unittest.mock import patch
from unittest import TestCase, main

class TestSearch(TestCase):

    ##############
    # UNIT TESTS #
    ##############

    def test_example_unit_test(self):
        # Storing into a variable so don't need to copy and paste long list every time
        # If you want to store search results into a variable like this, make sure you pass a copy of it when
        # calling a function, otherwise the original list (ie the one stored in your variable) might be
        # mutated. To make a copy, you may use the .copy() function for the variable holding your search result.
        expected_dog_search_results = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']
        self.assertEqual(search('dog'), expected_dog_search_results)


    def test_search(self):
        self.assertEqual(search(""),[])
        self.assertEqual(search("xyz"),[])
        self.assertEqual(search("DOG"),['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)'])
        self.assertEqual(search("a"),['List of Canadian musicians', 'Edogawa, Tokyo', 'Spain national beach soccer team', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Medical value travel', 'Lights (musician)', 'List of soul musicians', 'Human computer', 'Aube (musician)', 'List of overtone musicians', 'Black dog (ghost)', 'USC Trojans volleyball', 'Tim Arnold (musician)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Embryo drawing', 'Arabic music', 'C Sharp (programming language)', 'List of Saturday Night Live musical sketches', 'Joe Becker (musician)', 'Aco (musician)', 'Geoff Smith (British musician)', 'Reflection-oriented programming', 'B (programming language)', 'Richard Wright (musician)', 'Voice classification in non-classical music', 'Dalmatian (dog)', 'List of dystopian music, TV programs, and games', 'Steve Perry (musician)', '2009 Louisiana Tech Bulldogs football team', 'David Gray (musician)', 'Craig Martin (soccer)', 'Georgia Bulldogs football', 'Time travel', 'Annie (musical)', 'Alex Turner (musician)', 'Python (programming language)', 'List of gospel musicians', 'Tom Hooper (musician)', 'Indian classical music', 'Lua (programming language)', 'Single-board computer', 'Mets de Guaynabo (volleyball)', "United States men's national soccer team 2009 results", 'Joseph Williams (musician)', 'The Hunchback of Notre Dame (musical)', 'China national soccer team', 'Covariance and contravariance (computer science)', 'Personal computer', 'The Mandogs', 'David Levi (musician)', 'Digital photography', 'George Crum (musician)', 'Georgia Bulldogs football under Robert Winston', 'Wildlife photography', 'Traditional Thai musical instruments', 'Landseer (dog)', 'Charles McPherson (musician)', 'Comparison of programming languages (basic instructions)', 'Paul Carr (musician)', 'Spawning (computer gaming)', 'Sean Delaney (musician)', 'Tony Kaye (musician)', 'Danja (musician)', 'Ruby (programming language)', 'List of computer role-playing games', 'Mode (computer interface)', 'List of video games with time travel', 'Semaphore (programming)', "Wake Forest Demon Deacons men's soccer"])


    def test_title_length(self):
        a = search('a')
        art = search("art")
        empty = search('')
        school = search('fisk')

        self.assertEqual(title_length(100,a),['List of Canadian musicians', 'Edogawa, Tokyo', 'Spain national beach soccer team', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Medical value travel', 'Lights (musician)', 'List of soul musicians', 'Human computer', 'Aube (musician)', 'List of overtone musicians', 'Black dog (ghost)', 'USC Trojans volleyball', 'Tim Arnold (musician)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Embryo drawing', 'Arabic music', 'C Sharp (programming language)', 'List of Saturday Night Live musical sketches', 'Joe Becker (musician)', 'Aco (musician)', 'Geoff Smith (British musician)', 'Reflection-oriented programming', 'B (programming language)', 'Richard Wright (musician)', 'Voice classification in non-classical music', 'Dalmatian (dog)', 'List of dystopian music, TV programs, and games', 'Steve Perry (musician)', '2009 Louisiana Tech Bulldogs football team', 'David Gray (musician)', 'Craig Martin (soccer)', 'Georgia Bulldogs football', 'Time travel', 'Annie (musical)', 'Alex Turner (musician)', 'Python (programming language)', 'List of gospel musicians', 'Tom Hooper (musician)', 'Indian classical music', 'Lua (programming language)', 'Single-board computer', 'Mets de Guaynabo (volleyball)', "United States men's national soccer team 2009 results", 'Joseph Williams (musician)', 'The Hunchback of Notre Dame (musical)', 'China national soccer team', 'Covariance and contravariance (computer science)', 'Personal computer', 'The Mandogs', 'David Levi (musician)', 'Digital photography', 'George Crum (musician)', 'Georgia Bulldogs football under Robert Winston', 'Wildlife photography', 'Traditional Thai musical instruments', 'Landseer (dog)', 'Charles McPherson (musician)', 'Comparison of programming languages (basic instructions)', 'Paul Carr (musician)', 'Spawning (computer gaming)', 'Sean Delaney (musician)', 'Tony Kaye (musician)', 'Danja (musician)', 'Ruby (programming language)', 'List of computer role-playing games', 'Mode (computer interface)', 'List of video games with time travel', 'Semaphore (programming)', "Wake Forest Demon Deacons men's soccer"])
        self.assertEqual(title_length(0,art),[])
        self.assertEqual(title_length(100000,school),['Fiskerton, Lincolnshire', 'Fisk University'])
        self.assertEqual(title_length(10,empty),[])
        self.assertEqual(title_length(20,a),['Edogawa, Tokyo', 'Kevin Cadogan', 'Medical value travel', 'Lights (musician)', 'Human computer', 'Aube (musician)', 'Black dog (ghost)', 'Embryo drawing', 'Arabic music', 'Aco (musician)', 'Dalmatian (dog)', 'Time travel', 'Annie (musical)', 'Personal computer', 'The Mandogs', 'Digital photography', 'Wildlife photography', 'Landseer (dog)', 'Paul Carr (musician)', 'Tony Kaye (musician)', 'Danja (musician)'])
        self.assertEqual(title_length(0,empty),[])

    def test_article_count(self):
        dog = search('dog')
        program = search('programming')
        space = search(' ')
        music = search('muSic')
        empty = search('')
        school = search('fisk')
        self.assertEqual(article_count(10,dog), ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football'])
        self.assertEqual(article_count(0, dog),[])
        self.assertEqual(article_count(2, space),['List of Canadian musicians', 'French pop music'])
        self.assertEqual(article_count(1,space),['List of Canadian musicians'])
        self.assertEqual(article_count(5,music),['List of Canadian musicians', 'French pop music', 'Noise (music)', '1922 in music', '1986 in music'])
        self.assertEqual(article_count(100,music),['List of Canadian musicians', 'French pop music', 'Noise (music)', '1922 in music', '1986 in music', '2009 in music', 'Rock music', 'Lights (musician)', 'List of soul musicians', 'Aube (musician)', 'List of overtone musicians', 'Tim Arnold (musician)', 'Peter Brown (music industry)', 'Old-time music', 'Arabic music', 'List of Saturday Night Live musical sketches', 'Joe Becker (musician)', 'Aco (musician)', 'Geoff Smith (British musician)', 'Richard Wright (musician)', 'Voice classification in non-classical music', '1936 in music', '1962 in country music', 'List of dystopian music, TV programs, and games', 'Steve Perry (musician)', 'David Gray (musician)', 'Annie (musical)', 'Alex Turner (musician)', 'List of gospel musicians', 'Tom Hooper (musician)', 'Indian classical music', '1996 in music', 'Joseph Williams (musician)', 'The Hunchback of Notre Dame (musical)', 'English folk music (1500–1899)', 'David Levi (musician)', 'George Crum (musician)', 'Traditional Thai musical instruments', 'Charles McPherson (musician)', 'Les Cousins (music club)', 'Paul Carr (musician)', '2006 in music', 'Sean Delaney (musician)', 'Tony Kaye (musician)', 'Danja (musician)', 'Texture (music)', 'Register (music)', '2007 in music', '2008 in music'])
        self.assertEqual(article_count(5 ,program),['C Sharp (programming language)', 'Reflection-oriented programming', 'B (programming language)', 'Python (programming language)', 'Lua (programming language)'])
        self.assertEqual(article_count(1,program),['C Sharp (programming language)'])

    
    def test_random_article(self):
        dog = search('dog')
        program = search('programming')
        space = search(' ')
        music = search('muSic')
        empty = search('')
        school = search('fisk')
        self.assertEqual(random_article(-5,dog),'Endoglin')
        self.assertEqual(random_article(-100,dog),'')
        self.assertEqual(random_article(50,space),'Fisk University')
        self.assertEqual(random_article(10,empty),'')
        self.assertEqual(random_article(0,music),'List of Canadian musicians')
        self.assertEqual(random_article(0, empty), '')

    def test_favorite_article(self):
        dog = search('dog')
        program = search('programming')
        space = search(' ')
        music = search('muSic')
        empty = search('')
        school = search('fisk')
        self.assertEqual(favorite_article('bull',dog),True)
        self.assertEqual(favorite_article('LANGUAGE',program),True)
        self.assertEqual(favorite_article("assert",music),False)
        self.assertEqual(favorite_article(' ',space),True)
        self.assertEqual(favorite_article('',dog),True)
        self.assertEqual(favorite_article('ba',program),True)

    def test_multiple_keywords(self):
        dog = search('dog')
        program = search('programming')
        space = search(' ')
        music = search('muSic')
        empty = search('')
        school = search('fisk')
        bulldog = search('bulldog')
        self.assertEqual(multiple_keywords('cat',dog),['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)', 'Voice classification in non-classical music'])
        self.assertEqual(multiple_keywords('cats',empty),[])
        self.assertEqual(multiple_keywords('dog',empty),['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)'])
        self.assertEqual(multiple_keywords('programming',space),['List of Canadian musicians', 'French pop music', 'Edogawa, Tokyo', 'Noise (music)', '1922 in music', 'Ken Kennedy (computer scientist)', '1986 in music', 'Spain national beach soccer team', 'Kevin Cadogan', 'Endogenous cannabinoid', '2009 in music', 'Rock music', 'Medical value travel', 'Lights (musician)', 'List of soul musicians', 'Human computer', 'Aube (musician)', 'List of overtone musicians', 'Black dog (ghost)', 'USC Trojans volleyball', 'Tim Arnold (musician)', '2007 Bulldogs RLFC season', 'Peter Brown (music industry)', 'Mexican dog-faced bat', 'Embryo drawing', 'Old-time music', 'Arabic music', 'C Sharp (programming language)', 'List of Saturday Night Live musical sketches', 'Joe Becker (musician)', 'Will Johnson (soccer)', 'Aco (musician)', 'Geoff Smith (British musician)', 'Fiskerton, Lincolnshire', 'Reflection-oriented programming', 'B (programming language)', 'Richard Wright (musician)', 'Voice classification in non-classical music', 'Dalmatian (dog)', '1936 in music', 'Guide dog', '1962 in country music', 'List of dystopian music, TV programs, and games', 'Steven Cohen (soccer)', 'Steve Perry (musician)', '2009 Louisiana Tech Bulldogs football team', 'David Gray (musician)', 'Craig Martin (soccer)', 'Georgia Bulldogs football', 'Time travel', 'Fisk University', 'Annie (musical)', 'Alex Turner (musician)', 'Python (programming language)', 'List of gospel musicians', 'Tom Hooper (musician)', 'Indian classical music', 'Sun dog', '1996 in music', 'Lua (programming language)', 'Single-board computer', 'Mets de Guaynabo (volleyball)', "United States men's national soccer team 2009 results", 'Joseph Williams (musician)', 'The Hunchback of Notre Dame (musical)', 'China national soccer team', 'Covariance and contravariance (computer science)', 'English folk music (1500–1899)', 'Personal computer', 'The Mandogs', 'David Levi (musician)', 'Scores (computer virus)', 'Digital photography', 'George Crum (musician)', 'Solver (computer science)', 'Georgia Bulldogs football under Robert Winston', 'Wildlife photography', 'Traditional Thai musical instruments', 'Landseer (dog)', 'Charles McPherson (musician)', 'Comparison of programming languages (basic instructions)', 'Les Cousins (music club)', 'Paul Carr (musician)', '2006 in music', 'Spawning (computer gaming)', 'Sean Delaney (musician)', 'Tony Kaye (musician)', 'Danja (musician)', 'Ruby (programming language)', 'Texture (music)', 'List of computer role-playing games', 'Register (music)', 'Mode (computer interface)', '2007 in music', 'List of video games with time travel', '2008 in music', 'Semaphore (programming)', "Wake Forest Demon Deacons men's soccer", 'C Sharp (programming language)', 'Reflection-oriented programming', 'B (programming language)', 'Python (programming language)', 'Lua (programming language)', 'Comparison of programming languages (basic instructions)', 'Ruby (programming language)', 'Semaphore (programming)'])
        self.assertEqual(multiple_keywords('dog',bulldog),['2007 Bulldogs RLFC season', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Georgia Bulldogs football under Robert Winston', 'Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)'])



    #####################
    # INTEGRATION TESTS #
    #####################

    @patch('builtins.input')
    def test_example_integration_test(self, input_mock):
        keyword = 'dog'
        advanced_option = 6

        # Output of calling display_results() with given user input. If a different
        # advanced option is included, append further user input to this list (after `advanced_option`)
        output = get_print(input_mock, [keyword, advanced_option])
        # Expected print outs from running display_results() with above user input
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nHere are your articles: ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']\n"

        # Test whether calling display_results() with given user input equals expected printout
        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_advanced_1(self, input_mock):
        self.maxDiff = None
        keyword = 'dog'
        option = 1
        user_response = 15

        output = get_print(input_mock, [keyword, option, user_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(option) + '\n' + print_advanced_option(option) + str(user_response) + "\n\nHere are your articles: ['Edogawa, Tokyo', 'Kevin Cadogan', 'Dalmatian (dog)', 'Guide dog', 'Endoglin', 'Sun dog', 'The Mandogs', 'Landseer (dog)']\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_advanced_2(self, input_mock):
        self.maxDiff = None
        keyword = 'dog'
        option = 2
        user_response = 5

        output = get_print(input_mock, [keyword, option, user_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(option) + '\n' + print_advanced_option(option) + str(user_response) + "\n\nHere are your articles: ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season']\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_advanced_3(self, input_mock):
        self.maxDiff = None
        keyword = 'dog'
        option = 3
        user_response = 3

        output = get_print(input_mock, [keyword, option, user_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(option) + '\n' + print_advanced_option(option) + str(user_response) + "\n\nHere are your articles: Black dog (ghost)\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_advanced_4(self, input_mock):
        self.maxDiff = None
        keyword = 'dog'
        advanced_option = 4
        advanced_user_response = 'bulldog'

        output = get_print(input_mock, [keyword, advanced_option, advanced_user_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_user_response) + "\n\nHere are your articles: ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']\n" + "Your favorite article is in the returned articles!\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_advanced_5(self, input_mock):
        self.maxDiff = None
        keyword = 'dog'
        option = 5
        user_response = 'apple'

        output = get_print(input_mock, [keyword, option, user_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(option) + '\n' + print_advanced_option(option) + str(user_response) + "\n\nHere are your articles: ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']\n"

        self.assertEqual(output, expected)

        
# Write tests above this line. Do not remove.
if __name__ == "__main__":
    main()