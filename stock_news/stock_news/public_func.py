def mapping(source_name):
    img_path = ['']
    if source_name == "www.reuters.com":
        path = "//p[contains(@data-testid,\"paragraph\")]/text()"
        img_path = ['//div[contains(@data-testid, "Image") and @class="primary-image__image__1zwAE"]/div/img/@src']

    elif source_name == "headlinesoftoday":
        path = '//div[@class="single-container"]//article//p/text()'
        img_path = ['//div[@class="single-featured"]//img[starts-with(@src,"http")]/@src',
                    '//*[@id="post-185359"]/div[1]/div[2]/a/img/@src']

    elif source_name == "scmp":
        path = '(//section[@data-qa="ContentBody-ContentBodyContainer"])[1]//*[@datatype="p"]/text()'
        img_path = ['//div[@data-qa = "ArticleImage-ImageContainer"]//img/@src']

    elif source_name == "aljazeera":
        path = ['//div[@class="wysiwyg wysiwyg--all-content css-ibbk12"]/p/text()','//div[@class="wysiwyg css-1kw180w"]//p/text()','//div[@class="gallery-content wysiwyg wysiwyg--all-content css-ibbk12"]//p/text()']
        img_path = ['//figure[@class="article-featured-image"]/div[@class="responsive-image"]/img/@src','//div[@class="responsive-image"]//img/@src']

    elif source_name == "feedburner":
        path = ['//div[@itemprop="articleBody"]/p/text()','//div[@id="article-body"]//p/text()']
        img_path = ['//div[@class="ins_instory_dv_cont"]/img/@src','//div[@class="partial figure"]//picture/img/@src']

    elif source_name == "skynews":
        path = '//div[@class="sdc-article-body sdc-article-body--story sdc-article-body--lead"]/p/text() | //div[@class="sdc-article-header__titles"]/p/text()'
        img_path = ['//img[@class="sdc-article-image__item"]/@src']

    elif source_name == "rt":
        path = '//div[@class="article__text text "]/p/text()'
        img_path = ['//div[contains(@class,"article__cover ")]//img[starts-with(@src,"http")]/@src']

    elif source_name == "www.bloomberg.com":
        raise ValueError('Still developing')

    elif source_name == "watchdoguganda":
        path = ['//div[@class="content-inner "]/p/text()','//div[@class="content-inner "]/p/span/text()']
        img_path = ['//div[@class="thumbnail-container"]/img[starts-with(@src,"http")]/@src','//div[@class="thumbnail-container"]/img/@src']

    elif source_name == "news24":
        path = '//div[@class="article__body NewsArticle"]/p/text()'
        img_path = ['//div[@class="article__featured-image NewsArticle"]/img[starts-with(@src,"http")]/@src',
                    '//div[@class="article__body NewsArticle"]/p/img[starts-with(@src,"http")]/@src',
                    '//div[@class="swiper-wrapper"]//img[starts-with(@src,"http")]/@src',
                    '//div[@class="ov-group"]//video/@poster']

    elif source_name == "Seeking Alpha":
        raise ValueError('Still developing')
        # path = '//div[@class="kk_iZ"]/p'

    elif source_name == "rawstory":
        path = '//div[@class="body-description"]/p/text()'
        img_path = ['//div[@class="widget__head"]//img[starts-with(@src,"http")]/@src']

    elif source_name == "time":
        path = '//div[@id="article-body"]/div[1]/p/text()'
        img_path = ['//div[contains(@class,"partial figure")]//picture/img[starts-with(@src,"http")]/@src',
                    '//div[@class="component hero"]//img[starts-with(@src,"http")]/@src']

    elif source_name == "CNBC Television":
        raise ValueError('Still developing')

    elif source_name == "cbsnews":
        path = '//section[@class="content__body"]/p/text()'
        img_path = ['//section[@class="content__body"]//figure//img[starts-with(@src,"http")]/@src']

    elif source_name == "thenexthint":
        path = '//div[@class="entry-content herald-entry-content"]/p/text()'
        img_path = [
            '//div[@class="herald-post-thumbnail herald-post-thumbnail-single"]//picture/img[starts-with(@src,"http")]/@src']

    elif source_name == "Market Watch":
        path = '//div[@id="js-article__body"]/p/text() | //div[@class="paywall"]/p/text()'
        img_path = ['//div[@class="article__inset-wrapper--lead js-lead-image"]//img/@src']

    elif source_name == "www.marketwatch.com":
        path = '//div[@id="js-article__body"]/p/text() | //div[@class="paywall"]/p/text()'  # 待检验
        img_path = ['//div[@class="article__inset-wrapper--lead js-lead-image"]//img/@src']

    elif source_name == "Business Insider":
        path = '//div[@class="content-lock-content"]/p/text() | //div[@class="content-lock-content"]/ul/li/text()'
        img_path = ['//figure[@class="figure image-figure-image  "]//img/@src']

    elif source_name == "easternherald'":
        path = '//div[@class="wpb_wrapper"]//div[@data-td-block-uid="tdi_105"]//p/text()'
        img_path = ['']
    # elif source_name =="thelocal":
    #     path = ""
    #     img_path = ['']
    else:
        raise ValueError('Please use other functions or they are still developing')
    return path,img_path






def web_scraping(df,source_name):
    df_source = df[df['source_name']==source_name].copy()
    source = df_source['news_url'].tolist()
    img_path = []
    if source_name == "www.reuters.com":
        path = "//p[contains(@data-testid,\"paragraph\")]"
        img_path = ['//div[contains(@data-testid, "Image") and @class="primary-image__image__1zwAE"]/div/img/@src']

    elif source_name == "headlinesoftoday":
        path = '//div[@class="single-container"]//article//p'
        img_path = ['//div[@class="single-featured"]//img[starts-with(@src,"http")]/@src',
                    '//*[@id="post-185359"]/div[1]/div[2]/a/img/@src']

    elif source_name == "scmp":
        path = '(//section[@data-qa="ContentBody-ContentBodyContainer"])[1]//*[@datatype="p"]'
        img_path = ['//div[@data-qa = "ArticleImage-ImageContainer"]//img/@src']

    elif source_name == "aljazeera":
        path = '//div[@class="wysiwyg wysiwyg--all-content css-ibbk12"]/p'
        img_path = ['//figure[@class="article-featured-image"]/div[@class="responsive-image"]/img/@src']

    elif source_name == "feedburner":
        path = ['//div[@itemprop="articleBody"]/p','//div[@id="article-body"]/div[@class="padded"]/p']
        img_path = ['//div[@class="ins_instory_dv_cont"]/img/@src','//div[@class="partial figure"]//picture/img/@src']

    elif source_name == "skynews":
        path = '//div[@class="sdc-article-body sdc-article-body--story sdc-article-body--lead"]/p | //div[@class="sdc-article-header__titles"]/p'
        img_path = ['//img[@class="sdc-article-image__item"]/@src']

    elif source_name == "rt":
        path = '//div[@class="article__text text "]/p'
        img_path = ['//div[contains(@class,"article__cover ")]//img[starts-with(@src,"http")]/@src']

    elif source_name == "www.bloomberg.com":
        raise ValueError('Still developing')

    elif source_name == "watchdoguganda":
        path = '//div[@class="content-inner "]/p'
        img_path = ['//div[@class="thumbnail-container"]/img[starts-with(@src,"http")]/@src']

    elif source_name == "news24":
        path = '//div[@class="article__body NewsArticle"]/p'
        img_path = ['//div[@class="article__featured-image NewsArticle"]/img[starts-with(@src,"http")]/@src',
                    '//div[@class="article__body NewsArticle"]/p/img[starts-with(@src,"http")]/@src',
                    '//div[@class="swiper-wrapper"]//img[starts-with(@src,"http")]/@src',
                    '//div[@class="ov-group"]//video/@poster']

    elif source_name == "Seeking Alpha":
        path = '//div[@class="kk_iZ"]/p'

    elif source_name == "rawstory":
        path = '//div[@class="body-description"]/p'
        img_path = ['//div[@class="widget__head"]//img[starts-with(@src,"http")]/@src']

    elif source_name == "time":
        path = '//div[@id="article-body"]/div[1]/p'
        img_path = ['//div[contains(@class,"partial figure")]//picture/img[starts-with(@src,"http")]/@src',
                    '//div[@class="component hero"]//img[starts-with(@src,"http")]/@src']

    elif source_name == "CNBC Television":
        raise ValueError('Still developing')

    elif source_name == "cbsnews":
        path = '//section[@class="content__body"]/p'
        img_path = ['//section[@class="content__body"]//figure//img[starts-with(@src,"http")]/@src']

    elif source_name == "thenexthint":
        path = '//div[@class="entry-content herald-entry-content"]/p'
        img_path = [
            '//div[@class="herald-post-thumbnail herald-post-thumbnail-single"]//picture/img[starts-with(@src,"http")]/@src']

    elif source_name == "Market Watch":
        path = '//div[@id="js-article__body"]/p | //div[@class="paywall"]/p'
        img_path = ['//div[@class="article__inset-wrapper--lead js-lead-image"]//img/@src']

    elif source_name == "www.marketwatch.com":
        path = '//div[@id="js-article__body"]/p | //div[@class="paywall"]/p'  # 待检验
        img_path = ['//div[@class="article__inset-wrapper--lead js-lead-image"]//img/@src']

    elif source_name == "Business Insider":
        path = '//div[@class="content-lock-content"]/p | //div[@class="content-lock-content"]/ul/li'
        img_path = ['//figure[@class="figure image-figure-image  "]//img/@src']

    elif source_name == "easternherald'":
        raise ValueError('Still developing')
        # path = '//div[@class="wpb_wrapper"]//div[@data-td-block-uid="tdi_105"]//p'
        # img_path = ['']
    # elif source_name =="thelocal":
    #     path = ""
    #     img_path = ['']
    else:
        raise ValueError('Please use other functions or they are still developing')
