from playwright.sync_api import sync_playwright


link = "https://www.fitchratings.com/search/?dateValue=customDate&dateRange=09012022-09302022&expanded=entity&filter.sector=Sovereigns&viewType=data"


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(link)

        entity = page.wait_for_selector(
            "div.column__four:nth-child(2) > div:nth-child(1)"
        )
        tab = page.wait_for_selector(".column--merge-a.entity-data table")

        e = entity.evaluate("node => node.innerText")
        tab = tab.evaluate("node => node.innerText")

        a = page.wait_for_selector(".column__main")
        a = a.evaluate("node => node.innerHTML")

        # print(e)
        print(a)

        browser.close()

main()
