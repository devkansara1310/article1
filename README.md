# article1


# print(list(obj))
    # article_id = Artical.objects.all().values('id')
    # article_id_list=[i['id'] for i in article_id]
    
    # print(article_id_list)
    # l=[]
    # for i in article_id_list:
    #     article_tag=Tag.objects.filter(artical_id=i).values('name','artical_id')
    #     # print(article_tag)
    #     l.append([i['name'] for i in article_tag])
    # print(l)
    # article_last=[]
    # for i in article_id_list:
    #     article_last.extend(Artical.objects.filter(id=i))
        
    
    # for i in range(len(article)):
    # data_for_template.append(
    #     {
    #         'mListObjA':mList.A,
    #         'mListObjB':mList.B,
    #         'uDictObj':uDict[i], # or i+1 for your example uDict
    #     }
    # )
    # article_tag = ArticalTag.objects.all().values('name','artical_id')
    # print(article_tag)
    # article_id1 = ArticalTag.objects.filter(id=7).values('artical_id','id','name')
    # print(article_id1)
    # print("xxxxx")
    # x=[item['id'] for item in objx]
    #   (obj)
    # print(x)
    # artical_tag = ArticalTag.objects.filter(artical__id=7)
    # id = Artical.objects.all().values_list('id', flat=True)
    
    # for i in id:
    #     object = Artical.objects.filter(id=i).values('id')
    #     objl=[item['id'] for item in object]
    #     for i in objl:
    #         artical_tag = ArticalTag.objects.filter(artical__id=i)
            # print(artical_tag)
    # objl=[item['artical'] for item in artical_tag]
    # print(artical_tag)
    # article=Artical.objects.all()
    # obj=ArticalTag.objects.all()
    # objx= ArticalTag.objects.values('artical_id').annotate(total=Count('artical_id'))
    # objl=[item['id'] for item in objx]
    # objy= ArticalTag.objects.values('artical_id').annotate(total=Count('artical_id'))
    # objy=ArticalTag.objects.filter(artical_id__in=[item['artical_id'] for item in objx])
    # list1=([item.artical_id for item in objy])
    # print(list1)
    # x1=[]
    # for i in list1:
    #     if i not in x1:
    #         x1.append(i)
    #     else:
    #         print(i,end=' ')
    # print(objx)
    
    # print(tags)

    # print(article)
