#Outline provided
#Code Additions - Himadri Narasimhamurthy
#CS76 - 19W - M&C

class CannibalProblem:
    def __init__(self, start_state=(3, 3, 1)):
        self.start_state = start_state
        self.goal_state = (0, 0, 0)

        #keeping track of total for opposites
        self.total_m = start_state[0]
        self.total_c = start_state[1]

    #this function gets the state from the opposite side
    def get_opp(self, state, boat_state=(0,0)):
        #we have the two cases to deal with the two rules

        if state[2] == 1:
            #this is the case where the boat does not count as safe
            boat = 0
            opp_state = (self.total_m - state[0], self.total_c - state[1], boat)
            return opp_state
        else:
            #this is the case where the boat is "safe"
            boat = 1
            opp_state = (self.total_m - state[0] - boat_state[0], self.total_c - state[1] - boat_state[1], boat)
            return opp_state

    # get successor states for the given state
    def get_successors(self, state, safe_boat):
        successors = []

        #boat is constant for all successors
        if state[2] == 1:
            boat = 0
        else:
            boat = 1

        #this is the brute force state generator
        if state[2] == 1:
            #send one
            if state[0]>=1:
                s1 = (state[0] - 1, state[1], boat)
                bs1 = (1, 0) # state of the boat

                if safe_boat:
                    if self.sb_safe(s1, bs1):
                        successors.append(s1)
                else:
                    if self.strictrules_safe(s1):
                        successors.append(s1)

            if state[1]>=1:
                s2 = (state[0], state[1] - 1, boat)
                bs2 = (0, 1)

                if safe_boat:
                    if self.sb_safe(s2, bs2):
                        successors.append(s2)
                else:
                    if self.strictrules_safe(s2):
                        successors.append(s2)

            #send 2
            if state[0] >= 1 and state[1] >= 1:
                s5 = (state[0] - 1, state[1] - 1, boat)
                bs5 = (1,1)

                if safe_boat:
                    if self.sb_safe(s5, bs5):
                        successors.append(s5)
                else:
                    if self.strictrules_safe(s5):
                        successors.append(s5)

            if state[0]>=2:
                s3 = (state[0] - 2, state[1], boat)
                bs3 = (2, 0)

                if safe_boat:
                    if self.sb_safe(s3, bs3):
                        successors.append(s3)
                else:
                    if self.strictrules_safe(s3):
                        successors.append(s3)

            if state[1]>=1:
                s4 = (state[0], state[1] - 2, boat)
                bs4 = (0,2)

                if safe_boat:
                    if self.sb_safe(s4, bs4):
                        successors.append(s4)
                else:
                    if self.strictrules_safe(s4):
                        successors.append(s4)

        #all of these are adding to state
        if state[2] == 0:
            if state[0]<self.total_m:
                s6 = (state[0] + 1, state[1], boat)
                bs6 = (1,0)

                if safe_boat:
                    if self.sb_safe(s6, bs6):
                        successors.append(s6)
                else:
                    if self.strictrules_safe(s6):
                        successors.append(s6)

            if state[0]<self.total_m - 1:
                s7 = (state[0] + 2, state[1], boat)
                bs7 = (2,0)

                if safe_boat:
                    if self.sb_safe(s7, bs7):
                        successors.append(s7)
                else:
                    if self.strictrules_safe(s7):
                        successors.append(s7)

            if state[1]<self.total_c:
                s8 = (state[0], state[1] + 1, boat)
                bs8 = (0,1)

                if safe_boat:
                    if self.sb_safe(s8, bs8):
                        successors.append(s8)
                else:
                    if self.strictrules_safe(s8):
                        successors.append(s8)
            if state[1]<self.total_c - 1:
                s9 = (state[0], state[1] + 2, boat)
                bs9 = (0,2)

                if safe_boat:
                    if self.sb_safe(s9, bs9):
                        successors.append(s9)
                else:
                    if self.strictrules_safe(s9):
                        successors.append(s9)

            if state[0]<self.total_m and state[1]<self.total_c:
                s10 = (state[0] + 1, state[1] + 1, boat)
                bs10 = (1,1)

                if safe_boat:
                    if self.sb_safe(s10, bs10):
                        successors.append(s10)
                else:
                    if self.strictrules_safe(s10):
                        successors.append(s10)

        return successors

        # you write this part. I also had a helper function
        #  that tested if states were safe before adding to successor list
    #rule 2 verifier function
    def sb_safe(self, state, boat_state):
        opp = self.get_opp(state, boat_state)
        #all the necessary conditions

        if state[1] <= state[0] and state[0]>=0 and state[0]<=self.total_m \
                and state[1]>=0 and state[1]<=self.total_c and state[2]>=0:

            if opp[1] <= opp[0] and opp[0]!=0:
                return True

            if opp[0] == 0:
                return True

        else:
            return False
    #normal rule verifier function
    def strictrules_safe(self, state):
        opp = self.get_opp(state)
        #checking the conditions but also checking the opposite connections
        if state[1] <= state[0] and state[0]>=0 and state[0]<=self.total_m \
                and state[1]>=0 and state[1]<=self.total_c and state[2]>=0:

            if opp[1] <= opp[0] and opp[0]!=0:
                return True

            if opp[0] == 0:
                return True

        #checks those for the opposite side connections
        if state[0] == 0:
            if opp[1] <= opp[0] and opp[0]!=0:
                return True

            if opp[0] == 0:
                return True

        else:
            return False

    #tests whether were at the goal
    def goal_test(self, state):
        if state[0] == 0 and state[1] == 0 and state[2] == 0 == 0:
            return True

    def __str__(self):
        string =  "Missionaries and cannibals problem: " + str(self.start_state)
        return string


## A bit of test code

if __name__ == "__main__":
    test_cp = CannibalProblem((5, 5, 1))
    print(test_cp.get_successors((5, 5, 1), True))
    print(test_cp)
