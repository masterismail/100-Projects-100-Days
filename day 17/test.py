class user:
    def __init__(self,user_id,username):
        self.userid = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self,user):
        user.followers=user.followers+1
        self.following=self.following+1
      

user1 = user("ismail","master")
user2 = user("tahseer","master1")

user1.follow(user2)
print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)

