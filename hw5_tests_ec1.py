#########################################
##### Name: Hiroyuki Makino         #####
##### Uniqname: mhiro               #####
#########################################

import unittest
import hw5_cards_ec1

class TestHand(unittest.TestCase):

    def test_initialize_Hand(self):
        '''
        Test that a hand is initialized properly
        '''
        c1 = hw5_cards_ec1.Card(0, 2)
        c2 = hw5_cards_ec1.Card(1, 1)
        c3 = hw5_cards_ec1.Card(2, 12)
        c4 = hw5_cards_ec1.Card(3, 6)
        c5 = hw5_cards_ec1.Card(0, 13)

        h = hw5_cards_ec1.Hand([c1, c2, c3, c4, c5]) # Initialize a hand with five cards

        self.assertIsInstance(h.init_cards, list)   # check the type of the Instance Attribute
        self.assertEqual(len(h.init_cards), 5)      # check the number of cards
        self.assertEqual(type(h.init_cards[0]), hw5_cards_ec1.Card) # check the type of the card 
        self.assertEqual(str(h.init_cards[1]), str(c2)) # check if the card corresponds to the input
        
    def testAddAndRemove(self):
        '''
        Test that add_card( ) and remove_card( ) behave as specified.
        '''
        c1 = hw5_cards_ec1.Card(0, 2)
        c2 = hw5_cards_ec1.Card(1, 1)
        c3 = hw5_cards_ec1.Card(2, 12)
        c4 = hw5_cards_ec1.Card(3, 6)
        c5 = hw5_cards_ec1.Card(0, 13)
        c6 = hw5_cards_ec1.Card(1, 3)

        list_init_cards = [c1, c2, c3, c4, c5]
        h1 = hw5_cards_ec1.Hand(list_init_cards) # Initialize a hand with five cards
        h2 = hw5_cards_ec1.Hand(list_init_cards) # Initialize a hand with five cards     
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
        Test that draw( ) works as specified.
        '''
        d = hw5_cards_ec1.Deck() # Initialize a deck
        h = hw5_cards_ec1.Hand([]) # Initialize a hand with no cards

        h.draw(d) # Draw a card from the deck
        self.assertEqual(len(h.init_cards), 1) # Check if one card is added
        self.assertEqual(len(d.cards), 51) # Check if the number of cards in the deck has decreased by one (side effect)
        self.assertTrue(str(h.init_cards[0]) not in [str(card) for card in d.cards]) # Check if the drawed card is not in the deck

if __name__=="__main__":
    unittest.main()