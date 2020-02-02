# accepts at least two arguments, a function and an interable thing
# whatever function you pass in, usually a lambda, it will run that lambda for each value in the iterable
# returns a map object of the new version

nums = [2,4,6,8,10]

doubles = list(map(lambda x: x*2 , nums))
print(doubles)



people = ["Talia", "Trevor", "Tyler"]

upper = list(map(lambda name: name.upper(), people))
print(upper)

