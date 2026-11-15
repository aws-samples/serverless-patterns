package com.aws.example.model;

import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.Size;

/**
 *
 * @author biswanath
 */
public class BookRequest {
    
    @NotNull(message="Title cannot be null")
    @Size(min=2, message = "Title must not be less than 2 characters")
    private String title;
    
	
    @NotNull(message="Author cannot be null")
    @Size(min=2, message = "Author must not be less than 2 characters")
    private String author;
    
    @NotNull(message="Category cannot be null")
    @Size(min=2, max=16, message="Category must not be less than 2 characters")
    private String category;
    
    @NotNull(message="Page Count cannot be null")
    private int pageCount;

    /**
     * @return the firstName
     */
    public String getTitle() {
        return title;
    }

    /**
     * @param title the title to set
     */
    public void setTitle(String title) {
        this.title = title;
    }

    /**
     * @return the author
     */
    public String getAuthor() {
        return author;
    }

    /**
     * @param author the author to set
     */
    public void setAuthor(String author) {
        this.author = author;
    }

    /**
     * @return the category
     */
    public String getCategory() {
        return category;
    }

    /**
     * @param category the category to set
     */
    public void setCategory(String category) {
        this.category = category;
    }

    /**
     * @return the pageCount
     */
    public int getPageCount() {
        return pageCount;
    }

    /**
     * @param pageCount the pageCount to set
     */
    public void setPageCount(int pageCount) {
        this.pageCount = pageCount;
    }
    
}