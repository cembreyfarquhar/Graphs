import random
from '../graph/graph' import Graph
print(random.randint(1, 3))

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        if numUsers <= avgFriendships:
            print('You need more users than avg friends')
            return

        totalFriendships = numUsers * avgFriendships
        users_left = numUsers
        friendship_counts = []
        while totalFriendships != 0 and users_left != 0:
            this_users_friendships = random.randint(0, totalFriendships)
            users_left -= 1
            friendship_counts.append(this_users_friendships)
            print(this_users_friendships)
            totalFriendships -= this_users_friendships
        if len(friendship_counts) < numUsers:
            remaining_users = numUsers - len(friendship_counts)
            for i in range(0, remaining_users):
                friendship_counts.append(0)
        print(friendship_counts)
        print(len(friendship_counts))
        # Add users
        # their names are just numbers :shrugs:

        for i in range(0, numUsers):
            addUser(i)

        # Create friendships

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
