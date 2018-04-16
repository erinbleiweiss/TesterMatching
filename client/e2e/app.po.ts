import { browser, by, element } from 'protractor';

export class TesterMatchingPage {
  navigateTo() {
    return browser.get('/');
  }

  getParagraphText() {
    return element(by.css('tm-root h1')).getText();
  }
}
