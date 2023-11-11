from playwright.async_api import async_playwright
from features.url_concatenate import freeagent_url
# from utils.secrets import username, password
import utils.secrets as secrets

async def main():
    async with async_playwright() as p:
        browser = await p.firefox.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://www.hockeyarena.net/en/login")

        # Enter credentials
        await page.fill('input#nickFull.nice60.nice60Small', secrets.username)
        await page.fill('input.nice60:nth-child(4)', secrets.password)

        # Click the get LOGIN button.
        await page.get_by_role('button', name='Login').click()
        
        # Even prospects CSS selector: 'tr.re:nth-child(1) > td:nth-child(1) > a:nth-child(1)'
        # Odd prospects CSS selector: 'tr.odd:nth-child(2) > td:nth-child(1) > a:nth-child(1)'

        # Loop through selectors
        selectors = [
            'tr.re:nth-child({}) > td:nth-child(1) > a:nth-child(1)',
            'tr.odd:nth-child({}) > td:nth-child(1) > a:nth-child(1)']

        for i in range(1, 3): ## how many players to bid from the list --set 12 for 11 players
                selector = selectors[(i - 1) % 2] #this line switches between indexes of selectors
                await page.goto(freeagent_url)
                await page.click(selector.format(i))
                print(f'I just clicked at {i}th player')
                ## raise the offer and confirm it    
                await page.get_by_role('button', name='Confirm').click()
                print(f'Bidding on a candidate number {i} on the list')
                await page.get_by_role('button', name='Yes').click()
                print(f'Bid entered successfully for player {i} on the list')
        #if you want to see the print statments in the console run "pytest -s"


        """ TO BE IMPLEMENTED --> Conditional checking to avoid outbidding yourself
        ### Check if string Iskre or IskreID or ??? in selector:
        # el = await page.wait_for_selector('/html/body/div/div/div/div[2]/form/table[2]/tbody/tr[3]/td/b[2]/a')
        # #el = await page.query_selector('/html/body/div/div/div/div[2]/form/table[2]/tbody/tr[3]/td/b[2]')
        # el1 = await el.locator('a:has-text("???")')
        # el2 = await el.locator('a:has-text("Iskre")')
        # if await el1.is_visible():
        #     with open('output.txt', 'w') as f:
        #         print("??? element is present in the selector.", file=f)
        # elif await el2.is_visible():
        #     with open('output.txt', 'w') as f:
        #         print("Iskre element is present in the selector.", file=f)

        # inner_html = await el.inner_html()
        # with open('output.txt', 'w') as f:
        #     print(inner_html, file=f)
        #     print(type(inner_html), file=f)
        #     if '???' in inner_html:
        #         print('The value ??? is present in the selector.', file=f)
        #     else:
        #         print('The value ??? is not present in the selector.', file=f)
        # Log the result somewhere
        
        # with open('output.txt', 'w') as f:
        #     print(el, file=f)
        #     print(type(el), file=f)

        # await page.click('a:has-text("???")')
        # await page.click('a:has-text("Iskre")')

        # text = await el.text()
        # if '11748' in text or 'Iskre' in text:
        #     print('The value is present in the selector.')
        # else:
        #     print('The value is not present in the selector.')
        """
        

        ### CLOSE BROWSER ###
        await browser.close()
