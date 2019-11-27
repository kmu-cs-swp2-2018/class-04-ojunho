# assn7보고서 

## testGuess.py

### def setUp(self):

    def setUp(self):

        #단어 세개로 증가. g2, g3는 중복된글자가 있는 경우, e,n이 중복적으로 들어있는 경우를 선정.
        self.g1 = Guess('default')
        self.g2 = Guess('assignment')
        self.g3 = Guess('enhance')

        self.list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                     'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                     'w', 'x', 'y', 'z']

가장 크게 변한 부분은 메소드를 처음과 다르게 사용하여 바꿨다는 것이다.
우선, 처음 코드를 작성하였을 때는 체크할 비밀 단어를 default 하나만 했고, 그 하나로 self.g1.displayCurrent(), self.g3.displayGuessed(), self.g2.currentStatus등 단어 하나를 맞추는 과정에서 메소드, 혹은 객체가 변하는 과정을 각각의 메소드별로, 각각의 객체별로 확인하기 위해 여러개의 테스트 메소드를 만들었다.

하지만 새로 작성한 코드에서는 def setUp(self):, def tearDown(self): 를 제외한다면 총 세개의 메소드가 있는데, 각각 단어별로 깔끔하게 메소드를 작성하였다. 기존에 여러개의 테스트 메소드로 나눠서 작성했던 확인을 메소드 하나로 옮겨서(def testguess1(self):), self.g1.displayCurrent(), .displayGuessed(), .currentStatus, .guessedChars, finished()를 하나의 테스트 메소드에서 한글자 한글자 맞춰나가는 과정에서 발생할 수 있는 오류들을 다뤄주었다.

즉, 가장 큰 변화는 비밀 단어의 갯수에 따른 메소드의 변화이다. 

그래서 def setUp(self): 에서는 단어 세개를 설정해주고, self.list를 만들어주는데 이 리스트의 기능을 사용하는
메소드는 def testguess1(self): 이다 이 self.list에는 소문자인 알파벳이 전부 있다. 즉, 이 리스트는 공백문자, 숫자, 대문자가 들어갔을 때를 확인해주기 위함이다.

### def testguess1(self):

    def testguess1(self):

        self.assertEqual(self.g1.displayCurrent(), '_ e _ _ _ _ _ ')
        self.assertEqual(self.g1.displayGuessed(), ' e n ')
        self.assertEqual(self.g1.currentStatus, '_e_____')
        self.assertEqual(self.g1.guessedChars, {'', 'e', 'n'})
        self.assertFalse(self.g1.finished())

        #self.g1.guess('a')
        self.assertTrue(self.g1.guess('a'))
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ _ ')
        self.assertEqual(self.g1.displayGuessed(), ' a e n ')
        self.assertEqual(self.g1.currentStatus, '_e_a___')
        self.assertEqual(self.g1.guessedChars, {'', 'a', 'e', 'n'})
        self.assertFalse(self.g1.finished())

        #self.g1.guess('t')
        self.assertTrue(self.g1.guess('t'))
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ t ')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t ')
        self.assertEqual(self.g1.currentStatus, '_e_a__t')
        self.assertEqual(self.g1.guessedChars, {'', 'a', 'e', 'n', 't'})
        self.assertFalse(self.g1.finished())

        #self.g1.guess('u')
        self.assertTrue(self.g1.guess('u'))
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u ')
        self.assertEqual(self.g1.currentStatus, '_e_au_t')
        self.assertEqual(self.g1.guessedChars, {'', 'a', 'e', 'n', 't', 'u'})
        self.assertFalse(self.g1.finished())

        #self.g1.guess('d')
        self.assertTrue(self.g1.guess('d'))
        self.assertEqual(self.g1.displayCurrent(), 'd e _ a u _ t ')
        self.assertEqual(self.g1.displayGuessed(), ' a d e n t u ')
        self.assertEqual(self.g1.currentStatus, 'de_au_t')
        self.assertEqual(self.g1.guessedChars, {'', 'a', 'd', 'e', 'n', 't', 'u'})
        self.assertFalse(self.g1.finished())

        #self.g1.guess('f')
        self.assertTrue(self.g1.guess('f'))
        self.assertEqual(self.g1.displayCurrent(), 'd e f a u _ t ')
        self.assertEqual(self.g1.displayGuessed(), ' a d e f n t u ')
        self.assertEqual(self.g1.currentStatus, 'defau_t')
        self.assertEqual(self.g1.guessedChars, {'', 'a', 'd', 'e', 'f', 'n', 't', 'u'})
        self.assertFalse(self.g1.finished())

        #self.g1.guess('z')
        self.assertFalse(self.g1.guess('z'))
        self.assertEqual(self.g1.displayCurrent(), 'd e f a u _ t ')
        self.assertEqual(self.g1.displayGuessed(), ' a d e f n t u z ')
        self.assertEqual(self.g1.currentStatus, 'defau_t')
        self.assertEqual(self.g1.guessedChars, {'', 'a', 'd', 'e', 'f', 'n', 't', 'u', 'z'})
        self.assertFalse(self.g1.finished())

        #self.g1.guess('l')
        self.assertTrue(self.g1.guess('l'))
        self.assertEqual(self.g1.displayCurrent(), 'd e f a u l t ')
        self.assertEqual(self.g1.displayGuessed(), ' a d e f l n t u z ')
        self.assertEqual(self.g1.currentStatus, 'default')
        self.assertEqual(self.g1.guessedChars, {'', 'a', 'd', 'e', 'f', 'l', 'n', 't', 'u', 'z'})
        self.assertTrue(self.g1.finished())

def testguess1(self): 는 default단어에 대한 추론과정이다. 한글자씩 문자를 넣어주며, 그 단어가 비밀 단어에 있는지 아닌지를 self.assertTrue(), self.assertFalse() 로 판단을 한다. 또 현재의 상황, 현재 쓰여진 단어들의 상황을 나타내는 메소드들을 판단한다. 또 실제 현재 상황을 나타내는 객체, 그리고 실제 사용된 단어들이 들어가는 집합 객체를 판단한다. 메소드들과 객체들을 판단할 때는 self.assertEqual( , )를 사용하여 확인한다. 
만약에 이 단어에 없는 문자를 넣고, 그에 예상되는 결과를 적어서 실제로 작동하는 결과랑 같은지를 판단하는 것이다.
즉 이 단어에 없는 문자를 넣었을때는 현재의 상황을 나타내는 메소드와 객체는 그대로, 그리고 사용한 단어를 보여주는 메소드와 객체는 변화를 주어서 결과가 실제로 같은지 확인을 하는 것이다. 그리고 그 와중에 assertFalse()로 문자가 틀렸는지도 확인하는 것이다.

그리고 문자를 하나하나씩 넣는 중간에 assertFalse(self.g1.finished())를 통해서 완성이 되지 않았음을 확인받고, 전부 넣어서 완성이 되었다고 생각할 때는 assertTrue(self.g1.finished())를 통해서 완성이 되었음을 확인받는다.


### def testguess2(self):

    def testguess2(self):
        self.assertEqual(self.g2.displayCurrent(), '_ _ _ _ _ n _ e n _ ')
        self.assertEqual(self.g2.displayGuessed(), ' e n ')
        self.assertEqual(self.g2.currentStatus, '_____n_en_')
        self.assertEqual(self.g2.guessedChars, {'', 'e', 'n'})
        self.assertFalse(self.g2.finished())

        self.assertTrue(self.g2.guess('a'))
        self.assertEqual(self.g2.displayCurrent(), 'a _ _ _ _ n _ e n _ ')
        self.assertEqual(self.g2.displayGuessed(), ' a e n ')
        self.assertEqual(self.g2.currentStatus, 'a____n_en_')
        self.assertEqual(self.g2.guessedChars, {'', 'a', 'e', 'n'})
        self.assertFalse(self.g2.finished())

        #s가 두번 나오는 단어가 한번에 처리가 잘 되는지 확인.
        self.assertTrue(self.g2.guess('s'))
        self.assertEqual(self.g2.displayCurrent(), 'a s s _ _ n _ e n _ ')
        self.assertEqual(self.g2.displayGuessed(), ' a e n s ')
        self.assertEqual(self.g2.currentStatus, 'ass__n_en_')
        self.assertEqual(self.g2.guessedChars, {'', 'a', 'e', 'n', 's'})
        self.assertFalse(self.g2.finished())

        # 이미 사용했던 단어 s를 넣었을 때를 확인.
        self.assertTrue(self.g2.guess('s'))
        # 37행에서 알 수 있듯이 이미 사용한 's'를 guess해도 True가 나온다. 단어에 있기 때문인 것 같다.
        self.assertEqual(self.g2.displayCurrent(), 'a s s _ _ n _ e n _ ')
        self.assertEqual(self.g2.displayGuessed(), ' a e n s ')
        self.assertEqual(self.g2.currentStatus, 'ass__n_en_')
        self.assertEqual(self.g2.guessedChars, {'', 'a', 'e', 'n', 's'})
        self.assertFalse(self.g2.finished())

        self.g2.guess('i')

        self.g2.guess('g')

        self.g2.guess('m')

        self.g2.guess('t')

        self.assertTrue(self.g2.finished())

testguess2의 단어는 'assignment'이다 이 단어는 원래부터 중복되는 문자 's'가 있기 때문에 이를 확인해보기 위해서 넣어주었다. 그래서 이것도 마찬가지로 처음 's'를 넣었을 때 두개 전부 들어가는지, 예상한 결과와 실제 작동 결과가 같은지를 확인받기 위해서 assertEqual()을 사용하여 확인해준다.

그리고 또 이미 사용했던 단어 's'를 넣었을 때를 확인한다.
마찬가지로 변화가 없기 때문에 바로 전단계에서 변화를 주지 않고, 비교를 하여 변하지 않았음을 확인받는 식으로 한다. 그리고 self.assertTrue(self.g2.guess('s'))를 했을때 정상적으로 돌아가는 것을 보아 True임을 알 수 있는데 이는 그냥 guess()를 하여 넣은 문자가 비밀단어에 있는지 없는지에 따라서 T,F를 반환하기 때문에 트루를 반환함을 알 수 있다.

그리고 결국에는 하나하나씩 넣어서 finished()까지 한 번 더 확인해주었다. 중간중간에도 끝나지 않았음을 false로 확인해주었다.


### def testguess3(self):

    # 숫자, 공백, 대문자, 를 넣어가면서 assertIn으로 확인.
    def testguess3(self):
        self.assertEqual(self.g3.displayCurrent(), 'e n _ _ n _ e ')
        self.assertFalse(self.g3.finished())

        #1. 공백을 넣어서 확인. >> 오류뜸.
        #self.assertIn(' ', self.list)

        #아무런 조건에도 걸리지 않아서 들어갈 수 있는 소문자 'a'는 self.list에 있기 때문에 됨.
        self.assertIn('a', self.list)

        #self.g3.displayCurrent()는 그대로임.
        self.assertEqual(self.g3.displayCurrent(), 'e n _ _ n _ e ')

        #2. 대문자를 넣어서 확인. >> 오류뜸.
        #self.assertIn('A', self.list)

        #그리고 대문자 'A'는 self.g3.guess('A')를 해서 확인 할때 이 단어에 없기때문에 assertFalse 했을 때 통과 한다.
        self.assertFalse(self.g3.guess('A'))

        #3. 숫자를 넣어서 확인. >> 오류뜸.
        #self.assertIn('1', self.list)

마지막 testguess3()은 앞에서 말했던 숫자, 공백, 대문자를 확인해주는 것이다.

미리 만들어두었던 self.list에 있는지 없는지를 확인하면 된다. 그래서 assertIn()을 사용하면 된다. 
주석으로 설명한 것과 같이 공백, 숫자, 대문자 전부 넣어가면서 했을 때 오류가 남을 확인했다. 이 방법으로 세가지 경우를 전부 걸러줄 수 있을 것이다.

