import openai

def prompt(size=10):
    openai.api_key = "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"

    # size = 10
    prompt = "Give me {0} many unique visually identifiable colors that exists in python's pygame library in HEX color format each element being a string separated only by a comma".format(
        size)
    # print(prompt)

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # print(response["choices"][0]["text"])
    arr = response["choices"][0]["text"]
    
    # print(response)
    
    arr = arr.strip('\n')
    arr = arr.strip()
    # print(type(arr))
    # print(arr)
    lis = arr.split(",")
    lis2 = lis
    for i in range(len(lis)):
        lis2[i] = lis[i].strip()[1:-1]

    # print(lis)
    return lis2

# arr = prompt()

# print(arr)
