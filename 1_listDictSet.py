val = 10;

print(type(val));

binVal = bin(val);

print(type(binVal));
print(binVal);

# binVal[1] = '4'; # string are immutable in python

binIntVal = int(binVal[2:]); # slice

print(type(binIntVal));
print(binIntVal);

def addNormal(a, b) :
    return a + b;

print(addNormal(5, 5));

addlambda = lambda a, b : a + b; # inline statement 

print(addlambda(3, 3));

#                       LIST
nums = [1, 2, 3, 4];
print(f"value of last element is {nums[-1]}");

print(nums);
nums += nums;
print(nums);

flag = 4 in nums;
if(flag) :
    print("present");
else :
    print("Not present")
    
nums.append('B');
nums.insert(0, 'A');
print(nums);
del(nums[-2]); # del val at provided index
print(nums);
nums.remove('B'); # removes the actual value
print(nums);
lastItem = nums.pop(); # removes and returns last element
print(lastItem, nums);
nums.remove('A');
nums.sort(reverse = True); # sorts only similar kind elements
print(nums);

#                   dictionary

mp = {};
mp["name"] = "james Bond";
mp["Id"] = "007";

for key, val in mp.items() :
    print(f"key is {key} and value is {val}")

print(mp["name"]);

n = len(nums);
for i in range(0, n, 1) :
    mp.setdefault(nums[i], 0); # if not present them initiate with zero
    mp[nums[i]] += 1;

print(mp);
mp.pop("name");
print(mp);
print("Id" in mp.keys());
print("Id" in mp.values());

#           set

st = {4, 2, 2, 1};
print(st);
st.add(3);
st.remove(3);
print(st);
    