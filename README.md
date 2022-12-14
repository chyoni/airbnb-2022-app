# Airbnb API

Airbnb Clone Backend

REST & GraphQL API of the Airbnb Clone using Django REST Framework and Graphene GraphQL

### API Actions

- [ ] List Rooms
- [ ] Filter Rooms
- [ ] Search By Coords
- [ ] Login
- [ ] Create Account
- [ ] See Room
- [ ] Add Room to Favourites
- [ ] See Favs
- [ ] See Profile
- [ ] Edit Profile

### Index

- #01 Init

- #02 Django serializer

- #03 Django restframework

- #04 Serializer many=True

- #05 Serialize nested model

- #06 Django restframework pagination

- #07 Django restframework (detail view)

- #08 Django restframework (class based view)

- #09 Django restframework (get, put, delete)

  - 보니까 Serializer의 save() 메소드를 호출할 때, Serializer의 인자로 뭘 주냐에 따라 create, update가 실행이되네 문서를 읽으면 더 자세히 알 수 있지만 여튼 그렇다.

- #10 Django restframework

  - PUT

- #11 Django restframework

  - User

- #12 ModelSerializer magic

  - 그냥 Serializer는 instance를 받냐 안받냐에 따라 create, update이 나눠졌는데, ModelSerializer를 쓰면 그냥 save() call하는 순간 알아서 update는 update해준다.

- #13 User favs

- #14 User favs (add, remove)

- #15 Create user

- #16 JWT encode

  ```bash
  pipenv install pyjwt
  ```

- #17 JWT decode

  - django restframework에서 JWT 인증 관련 API가 잘 되어있다.
  - 참고 문서: https://www.django-rest-framework.org/api-guide/authentication/#authentication
  - 참고 문서: https://www.django-rest-framework.org/api-guide/authentication/#custom-authentication

- #18 Room search 1

- #19 Room search 2

- #20 Room search 3

  - lat, lng search

- #21 SerializerMethodField()

  - 이건 Dynamic field라고도 하는데, 만약 내가 어떤 오브젝트를 관심목록에 등록했다면 등록했는지 안했는지 serializer의 동적 필드를 사용해서 알아내는 방법이다.
