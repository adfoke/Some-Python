registry = []
def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func
@register
def f1():
    print('running f1()')

@register
def f2():
    print('running f2()')

def f3():
    print('running f3()')
def main1():
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()

#函数装饰器在导入模块时立即执行，而被装饰的函数只在明确调用时运行
#import decorate_demo
if __name__=='__main__':
    main1()