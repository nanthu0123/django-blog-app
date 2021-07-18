'''
view is Python function or class that takes a web request and return a web response.
Views are used to do things like fetch objects from the database,
modify those objects if needed, render forms, return HTML, and much more
'''

from datetime import datetime
from django.shortcuts import render
from blog.models import BlogPost


def home(request):
    '''function to reterive all blog data'''
    # get the all records from db table
    # pylint:disable=no-member
    blog_post_all = BlogPost.objects.all()
    if blog_post_all.exists():
        # iterate the every records then send it ti the user
        blog_data = []
        for data in blog_post_all:
            blog_data.append(data)
        return render(request, 'home.html', {'blog_data': blog_data})

    # if no records in db table, send the message to the user
    return render(request, 'home.html', {'message': 'no blog data'})


def create_blog(request):
    '''function for create blog post by user'''
    if request.method == 'POST':
        # get the form data
        title = request.POST['title']
        description = request.POST['description']
        author = request.POST['author']
        reference_link = request.POST['referenceLink']
        # filter the records based on form title
        # pylint:disable=no-member
        blog_post_title_filtered = BlogPost.objects.filter(Title=title)
        if blog_post_title_filtered.exists():
            # if form title already exist with title in record send the message to user
            return render(request, 'createBlog.html',
                          {'message': 'already has a blog post in same title'})
        # else save the form data to db
        # pylint:disable=no-member
        blog_post = BlogPost(Title=title, Description=description,
                             Author=author, ReferenceLink=reference_link)
        blog_post.save()
        return render(request, 'createBlog.html', {'message': 'blog has been posted'})

    return render(request, 'createBlog.html')


def search_blog(request):
    '''function for search a blog post by blog title contained character'''
    if request.method == 'POST':
        # get the blog title from form data
        blog_title = request.POST['BlogTitle']
        if blog_title:
            # if blog title in db table contains
            # character from title of form data, filter the records
            #pylint: disable=no-member
            blog_post_title_contained = BlogPost.objects.filter(
                Title__icontains=blog_title)

            if blog_post_title_contained.exists():
                # there is chance to more records in blog_post_title_contained,
                # so iterate the each records then send it to the user
                blog_data = []
                for data in blog_post_title_contained:
                    blog_data.append(data)
                return render(request, 'searchBlog.html',
                              {'blog_data': blog_data})
            # if no record matches the send message to the user
            return render(request, 'searchBlog.html', {'message': 'no blog data for this title'})

        print('no input search data')

    return render(request, 'searchBlog.html')


def update_blog(request, _pk):
    '''function for update the individual blog post by user'''

    if request.method == 'POST':
        # get the form data from updateBlog template
        title = request.POST['title']
        description = request.POST['description']
        author = request.POST['author']
        reference_link = request.POST['referenceLink']
        # update blog post and save the blog to db
        BlogPost.objects.filter(Id=_pk).update(Title=title, Description=description, Author=author,  # pylint:disable=no-member
                                               ReferenceLink=reference_link,
                                               CreatedDate=datetime.today().strftime('%Y-%m-%d'))
        return render(request, 'updateBlog.html', {'message': 'your blog has been updated'})
    # get the blog post based on primary key
    # pylint:disable=no-member
    blog_post_filter = BlogPost.objects.filter(
        Id=_pk)
    if blog_post_filter.exists():  # pylint:disable=no-else-return
        # if blog post exist for the primary key, send the blog post record to user
        return render(request, 'updateBlog.html', {'blog_post_filter': blog_post_filter})
    else:
        print('no data for this primary key')
    return render(request, 'updateBlog.html')


def delete_blog(request, _pk):
    '''function to delete the individual blog post by user'''
    if request.method == 'POST':
        # in post method get the primary key from url parameter,
        # filter the record based on _pk then delete the record
        BlogPost.objects.filter(Id=_pk).delete()  # pylint:disable=no-member
        return render(request, 'deleteBlog.html', {'message': 'blog post has been deleted'})

    return render(request, 'deleteBlog.html')
