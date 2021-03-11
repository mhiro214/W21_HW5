#########################################
##### Name: Hiroyuki Makino         #####
##### Uniqname: mhiro               #####
#########################################

import unittest
import hw5_cards_ec2

class TestHand(unittest.TestCase):

    def test_initialize_Hand(self):
        '''
        Test that a hand is initialized properly
        '''
        c1 = hw5_cards_ec2.Card(0, 2)
        c2 = hw5_cards_ec2.Card(1, 1)
        c3 = hw5_cards_ec2.Card(2, 12)
        c4 = hw5_cards_ec2.Card(3, 6)
        c5 = hw5_cards_ec2.Card(0, 13)

        h = hw5_cards_ec2.Hand([c1, c2, c3, c4, c5]) # Initialize a hand with five cards

        self.assertIsInstance(h.init_cards, list)   # check the type of the Instance Attribute
        self.assertEqual(len(h.init_cards), 5)      # check the number of cards
        self.assertEqual(type(h.init_cards[0]), hw5_cards_ec2.Card) # check the type of the card 
        self.assertEqual(str(h.init_cards[1]), str(c2)) # check if the card corresponds to the input
        
    def testAddAndRemove(self):
        '''
        Test that add_card( ) and remove_card( ) behave as specified.
        '''
        c1 = hw5_cards_ec2.Card(0, 2)
        c2 = hw5_cards_ec2.Card(1, 1)
        c3 = hw5_cards_ec2.Card(2, 12)
        c4 = hw5_cards_ec2.Card(3, 6)
        c5 = hw5_cards_ec2.Card(0, 13)
        c6 = hw5_cards_ec2.Card(1, 3)

        list_init_cards = [c1, c2, c3, c4, c5]
        h1 = hw5_cards_ec2.Hand(list_init_cards) # Initialize a hand with five cards
        h2 = hw5_cards_ec2.Hand(list_init_cards) # Initialize a hand with five cards     
        num_init_cards = len(h1.init_cards) 

        # Test add_card()
        h1.add_card(c3) # Add the card that is already in the hand
        self.assertEqual(len(h1.init_cards), num_init_cards) # Check if the number of cards does not change
        h1.add_card(c6) # Add a new card
        self.assertEqual(len(h1.init_cards), num_init_cards + 1) # Check if the number of cards has increased by one
        self.assertTrue(str(c6) in [str(card) for card in h1.init_cards]) # Check if the new card is in the hand
        

        # Test remove_card() 
        h2.remove_card(c6) # Remove a card that is not in the hand
        self.assertEqual(len(h2.init_cards), num_init_cards) # Check if the number of cards does not change
        removed_card = h2.remove_card(c4) # Remove the card that is in the hand
        self.assertEqual(len(h2.init_cards), num_init_cards-1) # Check if the number of cards has decreased by one
        self.assertEqual(str(removed_card), str(c4)) # Check if the removed card is correct
    
    def test_draw(self):
        '''
        Test that draw( ) works as specified
        '''
        d = hw5_cards_ec2.Deck() # Initialize a deck
        h = hw5_cards_ec2.Hand([]) # Initialize a hand with no cards

        h.draw(d) # Draw a card from the deck
        self.assertEqual(len(h.init_cards), 1) # Check if one card is added
        self.assertEqual(len(d.cards), 51) # Check if the number of cards in the deck has decreased by one (side effect)
        self.assertTrue(str(h.init_cards[0]) not in [str(card) for card in d.cards]) # Check if the drawed card is not in the deck

    def test_remove_pairs(self):
        '''
        Test that remove_pairs() works as specified
        '''
        # Case 1: 13 pairs & 0 unpaired cards
        d1 = hw5_cards_ec2.Deck() 
        h1 = hw5_cards_ec2.Hand(d1.deal_hand(13*2))
        h1.remove_pairs()
        self.assertEqual(len(h1.init_cards), 0) 

        # Case 2: 13 pairs & 6 unpaired cards (7 pairs & 6 three of a kind)
        d2 = hw5_cards_ec2.Deck() 
        h2 = hw5_cards_ec2.Hand(d2.deal_hand(13*2+6))
        h2.remove_pairs()
        self.assertEqual(len(h2.init_cards), 6) 

        # Case 3: no pairs & 7 unpaired cards
        d2 = hw5_cards_ec2.Deck() 
        h2 = hw5_cards_ec2.Hand(d2.deal_hand(7))
        h2.remove_pairs()
        self.assertEqual(len(h2.init_cards), 7) 

        # Case 4: 7 four of a kind & 6 three of a kind
        d3 = hw5_cards_ec2.Deck() 
        h3 = hw5_cards_ec2.Hand(d3.deal_hand(13*3+7))
        h3.remove_pairs()
        self.assertEqual(len(h3.init_cards), 6) 

    def test_deal(self):
        '''
        Test that deal() works as specified
        '''

        # Case 1: 5 hands,  5 cards per hand 
        d1 = hw5_cards_ec2.Deck()
        list_hands = d1.deal(num_hands=5, hand_size=5)
        self.assertEqual(type(list_hands[0]), hw5_cards_ec2.Hand) # Check if the element is Hand
        self.assertEqual(len(list_hands), 5) # Check the number of hands
        self.assertEqual(len(list_hands[0].init_cards), 5) # Check the hand size
        self.assertEqual(len(d1.cards), 52-5*5) # Check the number of cards in the deck

        # Case 2: 5 hands, all of the cards are dealt (i.e. hand_size=-1)
        d2 = hw5_cards_ec2.Deck()
        list_hands = d2.deal(num_hands=5, hand_size=-1)
        self.assertEqual(type(list_hands[0]), hw5_cards_ec2.Hand) # Check if the element is Hand
        self.assertEqual(len(list_hands), 5) # Check the number of hands
        list_hand_size = [len(hand.init_cards) for hand in list_hands]
        correct_list_hand_size = [11, 11, 10, 10, 10]
        self.assertTrue(list_hand_size == correct_list_hand_size) # Check the hand size
        self.assertEqual(len(d2.cards), 0) # Check the number of cards in the deck


if __name__=="__main__":
    unittest.main()