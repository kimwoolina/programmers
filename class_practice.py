# 클래스 사용 예제

# 추가 도전 과제:
# 1. input을 이용하여 Member 인스턴스 만드는것을 사용자가 터미널에서 할 수 있게 해주세요.
# 2. post도 터미널에서 생성할 수 있게 해주세요.
# 3. (심화)비밀번호 해싱이 무엇인지 공부한 후 hashlib 라이브러리를 써서 회원 비밀번호를 해시화하여 저장하게 해주세요.

class Member:
    def __init__(self, name, username, password):
        self.name = name            # 회원 이름
        self.username = username    # 회원 아이디
        self.password = password

    # 회원 정보 print(회원이름과 아이디만 보여주고 비밀번호는 보여줘서는 안됩니다!)
    def display(self):
        print(f"회원 이름 : {self.name}, 회원 아이디: {self.username}")


class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author        # 작성자 Member.username


# 맴버 리스트 생성 및 객체 생성
members = []
members.append(Member("김우린", "kimwoolina", 1234))
members.append(Member("이상현", "sanghyun", 3456))
members.append(Member("이새예", "saeye", 6789))

# 회원 이름 출력
for member in members:
    print(member.name)


# 게시글 리스트 생성 및 게시글 객체 생성
posts = []
posts.append(Post("Title 1", "content of post 1 by Lina Kim", "kimwoolina"))
posts.append(Post("Title 2", "content of post 2 by Lina Kim", "kimwoolina"))
posts.append(Post("Title 3", "content of post 3 by Lina Kim", "kimwoolina"))
posts.append(Post("Title 4", "content of post 4 by Sanghyun Lee", "sanghyun"))
posts.append(Post("Title 5", "content of post 5 by Sanghyun Lee", "sanghyun"))
posts.append(Post("Title 6", "content of post 6 by Sanghyun Lee", "sanghyun"))
posts.append(Post("Title 7", "content of post 7 by Saeye Lee", "saeye"))
posts.append(Post("Title 8", "content of post 8 by Saeye Lee", "saeye"))
posts.append(Post("Title 9", "content of post 9 by Saeye Lee", "saeye"))

# 특정유저(kimwoolina)가 작성한 게시글의 제목을 모두 프린트
# ‘특정 단어’가 content에 포함된 게시글의 제목을 모두 프린트
for post in posts:
    if post.author == "kimwoolina":
        print(f"kimwoolina님의 작성한 게시글: {post.title}")
    
    if  "Lee" in post.content :
        print(f"글 내용에 'Lee'가 포함된 게시글: {post.title}")

