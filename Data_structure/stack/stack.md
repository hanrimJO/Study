## Stack

- Last In First Out 의 LIFO 구조이다.
![stack](https://lh3.googleusercontent.com/proxy/ctLho3yobFXCnvZ4tuQtO_JbPHc3hd5LHv4sE7LAHdQw1DfJTh5VAiKKdWV5BDSw2mSX5XNGZFntZ9OCkNKQHr20vYWTO9G7AlS6sjUztJdv_r16MtWD7hZwe00Vr8IYv3hS-_q4qWLxQ4Ti-dAV2-aG04mK0MtvijUkB_7Bvcg4jLaxAgOUZ-Z45bMf8MjYQ_ClPkU8CoJ1b4xqE5RxG6bJNwPVMzZnK5Wx_8HgrHbtWJuN8Kf2qVzB2oxAB9zzTTLXs-728u6ccwzZ-d9hVQ7t8L4BqqwYqMhj)
- 브라우저로 치면 웹서핑중 뒤로가기를 누른 것과 같은 방식

- Stack 에서 data를 넣는 것을 push, 데이터를 꺼내는것을 pop 이라고 한다.
- push 와 pop 을 하는 위치는 맨윗 부분이기 때문에 그 위치를 top 으로 부른다.
- 스택의 가장 아랫부분은 bottom 이라고 칭한다.
- 파이썬은 보통 스택을 표현할때 list 를 사용한다.
    - push는 append, pop은 pop
    - pop사용시 top에 있는 값을 빼냄과 동시에 그 값을 리턴한다.

- 클래스로 스택을 구현해보면

```python
class Stack:
    def __init__(self):
        self.stack_items = []

    def push(self, x):
        self.stack_items.append(x)

    def pop(self):
        item_length = len(self.stack_items)
        if item_length < 1:
            print('Stack is Empty')
            return False
        result = self.stack_items[item_length-1]
        del self.stack_items[item_length-1]
        return result

    def isEmpty(self):
        return not self.stack_items
```
