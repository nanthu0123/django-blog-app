from django.shortcuts import render
from blog.models import BlogPost
from datetime import datetime


def home(request):
    # get the all records from db table
    blogPostAll = BlogPost.objects.all()
    if blogPostAll:
        # iterate the every records then send it ti the user
        blogData = []
        for data in blogPostAll:
            blogData.append(data)
        return render(request, 'home.html', {'blogData': blogData})
    else:
        # if no records in db table, send the message to the user
        return render(request, 'home.html', {'message': 'no blog data'})


def createBlog(request):
    if request.method == 'POST':
        # get the form data
        title = request.POST['title']
        description = request.POST['description']
        author = request.POST['author']
        referenceLink = request.POST['referenceLink']
        # filter the records based on form title
        blogPostTitleFiltered = BlogPost.objects.filter(Title=title)
        if blogPostTitleFiltered:
            # if form title already exist with title in record send the message to user
            return render(request, 'createBlog.html', {'message': 'already has a blog post in same title'})
        # else save the form data to db
        blogPost = BlogPost(Title=title, Description=description,
                            Author=author, ReferenceLink=referenceLink)
        blogPost.save()
        return render(request, 'createBlog.html', {'message': 'blog has been posted'})

    return render(request, 'createBlog.html')


def searchBlog(request):
    if request.method == 'POST':
        # get the blog title from form data
        blogTitle = request.POST['BlogTitle']
        if blogTitle:
            # if blog title in db table contains character from title of form data, filter the records
            blogPostTitleContained = BlogPost.objects.filter(
                Title__icontains=blogTitle)
            print(blogPostTitleContained)
            if blogPostTitleContained:
                # there is chance to more records in blogPostTitleContained, so iterate the each records then send it to the user
                blogData = []
                for data in blogPostTitleContained:
                    blogData.append(data)
                return render(request, 'searchBlog.html', {'blogData': blogData})
            else:
                # if no record matches the send message to the user
                return render(request, 'searchBlog.html', {'message': 'no blog data for this title'})
        else:
            print('no input search data')

    return render(request, 'searchBlog.html')


def updateBlog(request, pk):
    if request.method == 'GET':
        # get the blog post based on primary key
        blogPostFilter = BlogPost.objects.filter(Id=pk)
        if blogPostFilter:
            # if blog post exist for the primary key, send the blog post record to user
            return render(request, 'updateBlog.html', {'blogPostFilter': blogPostFilter})
        else:
            print('no data for this primary key')

        return render(request, 'updateBlog.html')

    elif request.method == 'POST':
        # get the form data from updateBlog template
        title = request.POST['title']
        description = request.POST['description']
        author = request.POST['author']
        referenceLink = request.POST['referenceLink']
        # update blog post and save the blog to db
        BlogPost.objects.filter(Id=pk).update(Title=title, Description=description, Author=author,
                                              ReferenceLink=referenceLink, CreatedDate=datetime.today().strftime('%Y-%m-%d'))
        return render(request, 'updateBlog.html', {'message': 'your blog has been updated'})


def deleteBlog(request, pk):
    if request.method == 'POST':
        # in post method get the primary key from url parameter, filter the record based on pk then delete the record
        BlogPost.objects.filter(Id=pk).delete()
        # redirect to home page
        # return redirect('home')
        return render(request, 'deleteBlog.html', {'message': 'blog post has been deleted'})

    return render(request, 'deleteBlog.html')
