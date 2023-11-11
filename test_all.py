import asyncio
from features.login import main
#from features.makeanoffer import makeAnOffer

def test_login():
    asyncio.run(main())

# def test_makeAnOffer():
#     asyncio.run(makeAnOffer())

