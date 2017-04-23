/*
 * (C) Copyright IBM Corporation 2006, 2007
 * All Rights Reserved.
 *
 * Permission is hereby granted, free of charge, to any person obtaining a
 * copy of this software and associated documentation files (the "Software"),
 * to deal in the Software without restriction, including without limitation
 * the rights to use, copy, modify, merge, publish, distribute, sub license,
 * and/or sell copies of the Software, and to permit persons to whom the
 * Software is furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice (including the next
 * paragraph) shall be included in all copies or substantial portions of the
 * Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT.  IN NO EVENT SHALL
 * THE COPYRIGHT HOLDERS, THE AUTHORS, AND/OR THEIR SUPPLIERS BE LIABLE FOR
 * ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
 * TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
 * OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 */

/**
 * \file glxbyteorder.h
 * Platform glue for handling byte-ordering issues in GLX protocol.
 *
 * \author Ian Romanick <idr@us.ibm.com>
 */
#if !defined(__GLXBYTEORDER_H__)
#define __GLXBYTEORDER_H__

#ifdef HAVE_DIX_CONFIG_H
#include <dix-config.h>
#endif

#include "misc.h"

static inline uint16_t
bswap_16(uint16_t val)
{
    swap_uint16(&val);
    return val;
}

static inline uint32_t
bswap_32(uint32_t val)
{
    swap_uint32(&val);
    return val;
}

static inline uint64_t
bswap_64(uint64_t val)
{
    swap_uint64(&val);
    return val;
}

#endif                          /* !defined(__GLXBYTEORDER_H__) */
