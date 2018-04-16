import { TesterMatchingPage } from './app.po';

describe('tester-matching App', () => {
  let page: TesterMatchingPage;

  beforeEach(() => {
    page = new TesterMatchingPage();
  });

  it('should display welcome message', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('Welcome to tm!!');
  });
});
